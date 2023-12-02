const fs = require("fs");
// const crypto = require("crypto");
const colors = require('colors');
const tldjs = require("tldjs");
// const config = require('./arguments').config;
const puppeteer = require('puppeteer');
const retire = require('retire');
const url_parse = require('url');
// const pageFunc = require('./apihook').pageFunc;

let chrome;
let client;
let page;

let seenScripts = new Map();
let networkTraces = new Map();
let debuggerTraces = new Map();
let customTraces = new Map();
let resolvedTraces = new Map();
let apiTraces = [];
let apiResults = new Map();

let libUrlHashes = new Set();
let StacktraceCache = new Map();
let ourInjectedSids = new Set();
let dynamicParserInserted = new Array();
let cspRoadblocks;


let retireRepo = JSON.parse(retire.replaceVersion((fs.readFileSync('retire.json')).toString()));


const pslCache = new Map();
let hostToColor = new Map();
let freeColors = ["blue", "magenta", "green", "red", "cyan", "yellow"];

async function main() {
    log('Starting chrome...');
    chrome = await puppeteer.launch();

    log('Setting up...');
    page = await chrome.newPage();
    client = await page.target().createCDPSession();
    await prepareChrome();

    log('Visiting', config.url);
    log('Please wait up to 30 seconds');
    await page.goto(config.url, {
        waitUntil: 'load',
        timeout: config.loadTimeout,
    }).catch((error) => {
        log('Site load failed with error:', error);
        abortCrawl();
    });

    await delay(config.afterTimeout);
    log('Loaded', page.url());

    await processScripts();
    await processApis();
    await checkForCspIssues();
    outputResults();
    process.exit();
}

/*
 * Setup
 */

async function prepareChrome() {
    chrome.on('disconnected', () => {
        log('Browser was disconnected...');
        abortCrawl();
    });

    await Promise.all([
        client.send("Debugger.enable"),
        client.send("Network.enable"),
        client.send("Runtime.enable"),
    ]);

    await client.send('Runtime.setAsyncCallStackDepth', {maxDepth: 50}).catch();

    client.on("Network.requestWillBeSent", async function (params) {
        if (!sameOrigin(params)) {
            return;
        }
        if (params.type == "Script" && params.initiator && params.initiator.stack) {
            //This event is triggered anew for every redirect
            networkTraces.set(params.request.url, params.initiator.stack);
        }
    });

    client.on("Runtime.consoleAPICalled", async function (params) {
        if (params.type != "log" || params.args.length == 0 || params.args[0].type != "string") {
            return;
        }
        // discard all entries not found in the main frame
        if ((await page.mainFrame()._contextPromise)._contextId != params.executionContextId) {
            return;
        }

        let message = params.args[0].value;
        if (params.stackTrace && message && message.startsWith("[Script]")) {
            let hash = message.substr(8);
            customTraces.set(hash, params.stackTrace);
        }
        if (params.stackTrace && message && message.startsWith("[SMURF]")) {
            let to_parse = message.substr(7);
            let parsed = JSON.parse(to_parse);
            parsed.stackTrace = params.stackTrace;
            apiTraces.push(parsed);
        }
        if (message && message.startsWith && message.startsWith('[ParserInserted]')) {
            let hashedId = message.slice(16);
            dynamicParserInserted.push(params.stackTrace);
        }
    });

    await client.on("Debugger.scriptParsed", async function (params) {
        if (!sameOrigin(params)) {
            return;
        }
        if (params.stackTrace) {
            debuggerTraces.set(params.scriptId, params.stackTrace);
        }
        let source = (await client.send("Debugger.getScriptSource", {scriptId: params.scriptId})).scriptSource;
        let script = {
            id: params.scriptId,
            url: params.url,
            hash: MD5(source),
            url_hash: MD5(params.url),
            source: source.substr(0, 200),
            stack: params.stackTrace
        };

        // puppeteer translation layer
        if (script.url === '__puppeteer_evaluation_script__') {
            ourInjectedSids.add(script.id);
            return;
        }

        // check for library
        if (source !== undefined) {
            // specifically injected scripts from us
            if (source.startsWith('/*SMURF*/')) {
                ourInjectedSids.add(script.id);
                return;
            }
            // puppeteer translation layer
            if (source.startsWith('(function deliverResult')) {
                ourInjectedSids.add(script.id);
                return;
            }
            // puppeteer translation layer
            if (source.startsWith('(function addPageBinding')) {
                ourInjectedSids.add(script.id);
                return;
            }

            let results = retire.scanFileContent(source, retireRepo, SHA1hasher);
            if (results.length > 0) {
                // we have a lib found
                libUrlHashes.add(script.url_hash);
            }
        }

        if (script.url !== '' && (params.startLine > 0 || params.startColumn > 0)) {
            // bogus script url
            script.url = '';
        }

        if (script.stack !== undefined && script.stack !== null) {
            if (script.stack.callFrames && script.stack.callFrames[0]) {
                // We are directly above our hooked functionality, which means that it is the calling entity -> discard
                // If we are otherwise in the callstack we are part of a composite callstack which already contains one indirection of eval thus also one of our functions
                if (script.stack.callFrames[0].functionName === '_hooked_eval' || script.stack.callFrames[0].functionName === '_hookedNodeInsertion') {
                    return

                }
                if (script.stack.callFrames[0].functionName === 'document.(anonymous function)') {
                    // Triggers on doc write which we already capture elsewhere
                    return
                }
            }
        }

        seenScripts.set(params.scriptId, script);
        if(!customTraces.has(script.hash) && !script.url && !(params.startColumn>0||params.startLine>0)&&!script.url && params.stackTrace) {
            // in essence if the script fulfills the following conditions:
            // 1) was not part of the initial document(does not have offset in the document)
            // 2) it does not have an url associated
            // 3) it is not part of our scripts(either via prepended COMMENT or __puppeteer_evaluation_script__ as url)
            // 4) the associated source can be retrieved via the debugger
            // 5) does not carry artifacts exhibited by other inclusions
            // Then we can conclude that it was an eval call
            apiTraces.push({stackTrace: params.stackTrace, tag:"eval"});
        }

    });
    await page.exposeFunction('__MD5', MD5);
    await page.evaluateOnNewDocument(pageFunc);
}

function MD5(st) {
    let md5sum = crypto.createHash('MD5');
    md5sum.update(st);
    return md5sum.digest('hex');
}

const SHA1hasher = {
    'sha1': function (data) {
        let shasum = crypto.createHash('sha1');
        shasum.update(data);
        return shasum.digest('hex');
    }
};

function sameOrigin(params) {
    let frameId = params.frameId;
    if (!frameId) {
        try {
            frameId = params.executionContextAuxData.frameId;
        } catch (e) {
            console.log(params.executionContextAuxData);
        }
    }

    for (let frame of page.frames()) {
        if (frame._id == frameId) {
            if (frame._url == "about:srcdoc" || pslHost(frame._url) == pslHost(page.url())) {
                return true;
            }
            return false;
        }
    }
    return false;
}

/*
 * Process data
 */

async function flattenStack(stack) {
    let cf = [];
    do {
        for (let frame of stack.callFrames) {
            cf.push(frame);
        }
        if (stack.parentId) {
            let id = stack.parentId.id;
            if (StacktraceCache.has(id)) {
                stack = StacktraceCache.get(id);
            }
            else {
                stack = await client.send('Debugger.getStackTrace', {stackTraceId: stack.parentId}).catch();
                StacktraceCache.set(id, stack);
            }

            if (stack)
                stack = stack.stackTrace;
        }
        else {
            stack = stack.parent;
        }
    } while (stack !== undefined);
    return cf;
}

function cleanOurSids(stack) {
    let cf = [];
    for (let frame of stack) {
        if (!ourInjectedSids.has(frame.scriptId)) {
            cf.push(frame);
        }
    }
    return cf
}

function getStos(frames) {
    // this may happen over cleaned stacktraces when we produce an api trace
    if (frames.length === 0) {
        return
    }
    for (let i = frames.length - 1; i >= 0; i--) {
        let frame = frames[i];
        let script = seenScripts.get(frame.scriptId);
        if (script && script.url && libUrlHashes.has(script.url_hash)) {
            continue
        }
        return script;
    }
    if (seenScripts.has(frames[frames.length - 1].scriptId)) {
        return seenScripts.get(frames[frames.length - 1].scriptId);
    }
    return undefined
}

async function processApis() {

    let length = apiTraces.length;

    for (let i = 0; i < length; i++) {
        let api = apiTraces[i];
        let flattened = await flattenStack(api.stackTrace);
        let cleaned = await cleanOurSids(flattened);
        let stos = getStos(cleaned);
        if (!stos) {
            continue;
        }

        // default to the loaded page if we cannot find another intermediate parent
        let host = url_parse.parse(page.url()).hostname;

        let associatedExternal = await findAssociatedExternalScript(stos);
        if (associatedExternal){
            host = url_parse.parse(associatedExternal.url).hostname;
        }

        if (apiResults.has(host)) {
            apiResults.get(host).add(api.tag);
        } else {
            apiResults.set(host, (new Set()).add(api.tag))
        }
    }

    // Check initially loaded scripts for inline scripts
    for (let sid of resolvedTraces.get(-1)) {
        if (!seenScripts.has(sid)) {
            continue
        }
        let directScript = seenScripts.get(sid);
        if (!directScript.url){
            let host = url_parse.parse(page.url()).hostname;
            if (apiResults.has(host)) {
                apiResults.get(host).add('inline_script');
            } else {
                apiResults.set(host, (new Set()).add('inline_script'))
            }
        }
    }

}

async function processScripts() {
    for (let script of seenScripts.values()) {
        let trace = findTrace(script);
        if (trace) {
            let flatten = await flattenStack(trace);
            let cleaned = await cleanOurSids(flatten);
            let stos = await getStos(cleaned);
            if (stos === undefined) {
                continue
            }
            if (resolvedTraces.has(stos.id)) {
                resolvedTraces.get(stos.id).add(script.id);
            }
            else {
                resolvedTraces.set(stos.id, (new Set()).add(script.id));
            }
        }
        else {
            // we did not find a trace => was directly written to the document
            if (resolvedTraces.has(-1)) {
                resolvedTraces.get(-1).add(script.id);
            }
            else {
                resolvedTraces.set(-1, (new Set()).add(script.id));
            }
        }
    }
}

function findTrace(script) {
    //The order is important, custom overrides dynamic
    if (customTraces.has(script.hash)) {
        return customTraces.get(script.hash);
    }
    else if (script.url && networkTraces.has(script.url)) {
        return networkTraces.get(script.url);
    }
    else if (debuggerTraces.has(script.id)) {
        return debuggerTraces.get(script.id);
    }
    return null;
}

async function checkForCspIssues() {
    const strictDynamicViolator = new Set();
    const inlineScriptWritingHosts = new Set();
    const inlineHandlerWritingHosts = new Set();
    const evalUsingHosts = new Set();

    // strict-dynamic violator
    for (let stackTrace of dynamicParserInserted) {
        let flattened = await flattenStack(stackTrace);
        let cleaned = await cleanOurSids(flattened);
        let stos = getStos(cleaned);
        if (!stos) {
            continue;
        }

        // default to the loaded page if we cannot find another intermediate parent
        let host = url_parse.parse(page.url()).hostname;

        let associatedExternal = await findAssociatedExternalScript(stos);
        if (associatedExternal){
            host = url_parse.parse(associatedExternal.url).hostname;
        }
        strictDynamicViolator.add(host);
    }

    // Now investigate unsafe-inline and unsafe-eval incompatibilities
    for (let host of apiResults.keys()){
        if (apiResults.get(host).has('inline_script')){
            inlineScriptWritingHosts.add(host);
        }
        if (apiResults.get(host).has('inline_handler')){
            inlineHandlerWritingHosts.add(host);
        }
        if (apiResults.get(host).has('eval')){
            evalUsingHosts.add(host);
        }
    }

    cspRoadblocks = {
        strictDynamicViolator,
        inlineScriptWritingHosts,
        inlineHandlerWritingHosts,
        evalUsingHosts
    }
}

async function findAssociatedExternalScript(script){
    let cur_script = script;
    while(!cur_script.url && !cur_script.url.startsWith('http')){
        // resolve parent
        let trace = findTrace(cur_script);
        if (trace) {
            let flatten = await flattenStack(trace);
            let cleaned = await cleanOurSids(flatten);
            let stos = await getStos(cleaned);
            if (stos === undefined) {
                return;
            }
            cur_script = stos;
        }else{
            return;
        }
    }
    // returns the identity if the input script was already an external one
    return cur_script;
}


/*
 * Present results
 */

function outputResults() {
    let count = 0;
    log('Inclusion analysis:');
    for (let sid of resolvedTraces.get(-1)) {
        //Reset between scripts as we otherwise will run out of colors
        hostToColor = new Map();
        freeColors = ["blue", "magenta", "green", "red", "cyan", "yellow", "white"];

        if (!seenScripts.has(sid)) {
            continue
        }
        let directScript = seenScripts.get(sid);
        let tree = [{sid: sid, url: directScript.url === '' ? page.url() : directScript.url, depth: 0}];
        let seen = (new Set()).add(sid);
        resolveRecursive(sid, 1, tree, seen);
        let buffer = printTree(tree);
        //Only show if at least two different third parties are part of the inclusion
        if (freeColors.length < 5) {
            count++;
            console.log(buffer);
        }
    }
    if (config.showApiResults) {
        console.log(config.sep);
        log('API analysis:');
        console.log(apiResults);
        console.log(config.sep);
    }
    if (config.showCspResults) {
        console.log(config.sep);
        log('CSP analysis:');
        console.log(cspRoadblocks);
        console.log(config.sep);
    }
    if (count === 0) {
        log("We could not find any scripts involving a minimum of two third parties!");
        log("For more results, try something like https://bbc.com/");
        console.log(config.sep);
    }
    else {
        outputNotes();
    }

}

function resolveRecursive(current, depth, result, seen) {
    // no more children of the current subtree
    if (!resolvedTraces.has(current)) {
        return;
    }
    for (let sid of resolvedTraces.get(current)) {
        let cur_depth = depth;
        if (!seenScripts.has(sid)) {
            continue
        }
        let childScript = seenScripts.get(sid);
        let url = childScript.url;
        if (seen.has(url)) {

        }
        else {
            result.push({url: url, depth: depth});
            cur_depth = cur_depth + 1;
        }
        seen.add(url);
        resolveRecursive(sid, cur_depth, result, seen);
    }
}


function printTree(tree) {
    if (tree.length == 0) {
        return;
    }
    let result = "";
    let padding = "===";
    for (let node of tree) {
        let str = "";
        if (node.depth > 0) {
            str += padding.repeat(node.depth) + "> ";
        }
        result += colorString(str + node.url + "\n", pslHost(node.url));
    }
    return result;
}

function outputNotes() {
    console.log(config.sep);
    log("Order (in each block)");
    log(" - The first URL caused the avalanche of inclusions, if it is the loaded URL it was initiated by an inline script");
    log(" - The last URL was the finally included script caused by all above it");
    log("Indentation");
    log(" - Indentation indicates inclusion depth");
    log(" - Same indentation indicates that one resource included multiple further resources");
    log("Colors");
    log(" - Same color means same party (uses eTLD+1 without extended same-party)");
    log(" - If more parties than colors available, grey is used for the remaining");
    log(" - Colors are reset between blocks");
    log("Trees are simplified to get useable output on the console");
    log(" - Only prints scripts with at least two different third parties in the subtree");
    console.log(config.sep);
}

/*
 * Helper stuff
 */

function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function log() {
    let adjusted = ['[SMURF]'];
    for (let i = 0; i < arguments.length; i++) {
        adjusted.push(arguments[i]);
    }
    console.log(...adjusted);
}

function colorString(str, host) {
    let color = hostToColor.get(host);
    if (!color) {
        color = freeColors.pop();
        hostToColor.set(host, color);
    }
    if (!color) {
        //If we run out of colors, use gray for the rest
        color = "gray";
    }
    return str[color];
}

function pslHost(host) {
    //Trivial if only one dot
    if (host.split(".").length <= 2) {
        return host;
    }

    if (pslCache.has(host)) {
        return pslCache.get(host);
    }
    let parsed = tldjs.getDomain(host);
    pslCache.set(host, parsed);
    return parsed;
}

function abortCrawl() {
    log('Unrecoverable Error, exiting...');
    process.exit(-1);
}

main();
