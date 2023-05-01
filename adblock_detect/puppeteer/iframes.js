// const fs = require('fs');
// var sites_dict = require("/home/ritik/work/pes/measurements/adblock_detect/inner_pages.json")
// var filename = "/home/ritik/work/pes/measurements/adblock_detect"

const puppeteer = require('puppeteer');
const Xvfb = require('xvfb');
// const sites = ["geeksforgeeks.org", "forbes.com", "insider.com"];
// var start_str = "http://";

var args = process.argv; // node iframes.js site extn

(async () => {
    var xvfb = new Xvfb({
        silent: true,
        reuse: true,
        // xvfb_args: ["-screen", "0", '1280x720x24', "-ac"],
    });
    xvfb.start((err)=>{if (err) console.error(err)});
    let p_args;
    if (args[3] === 'control'){
        p_args = [
            "--disable-gpu",
            "--disable-dev-shm-usage",
            "--no-sandbox",
            '--disable-web-security',
            '--disable-features=IsolateOrigins,site-per-process',
            // `--load-extension=/home/ritik/work/pes/extensions/privacy_extn/${args[3]}`,
            '--display='+xvfb._display,
            '--window-size=960, 1080',
            '--disable-features=AudioServiceOutOfProcess'
        ];
    }
    else{
        p_args= [
            "--disable-gpu",
            "--disable-dev-shm-usage",
            "--no-sandbox",
            '--disable-web-security',
            '--disable-features=IsolateOrigins,site-per-process',
            `--load-extension=/home/ritik/work/pes/extensions/privacy_extn/${args[3]}`,
            '--display='+xvfb._display,
            '--window-size=960, 1080',
            '--disable-features=AudioServiceOutOfProcess'
        ];
    }
    const browser = await puppeteer.launch({ 
        headless: false,
        ignoreDefaultArgs: ["--disable-extensions","--enable-automation"],
        args: p_args,
        executablePath: '/usr/bin/google-chrome' 
        // executablePath: '/snap/bin/chromium' 
    });
    const page = await browser.newPage();
    await page.setViewport({ width: 960, height: 1080 });
    await page.waitForTimeout(10000);
    var sites = args[2].split(',');
    // console.log(sites)
    for (let index=0; index<sites.length; index++){
    // for (let index=0; index<1; index++){
        let site = sites[index];
        try{
            await page.goto(site, { waitUntil: 'networkidle2', timeout: 60000 });
            await page.waitForTimeout(2000);
        } catch (error){
            console.error(error);
            console.log(site);
            // continue;
            break;
        }
        
        let source = await page.content();
        source = source.toLowerCase();
        var match = "";
        if (source.includes('ad-blocker')){
            match = 'ad-blocker';
        } else if (source.includes('ad blocker')){
            match = 'ad blocker';
        } else if (source.includes(' adblocker ')){
            match = ' adblocker ';
        } else if (source.includes('adblock.detect')){
            match = 'adblock.detect';
        }

        if (match !== ""){
            const arr = source.split(match)
            let pgsrc1 = arr[0].substr(arr[0].length - 30)
            let pgsrc2 = arr[1].slice(0,30)
            let pgsrc = pgsrc1 + match + pgsrc2

            await page.screenshot({path: `ss/${args[3]}/${args[4]}.png`});
            console.log(`adblocker_detected: ${site} ${args[3]}  ${pgsrc}`);
            break;
        }
        else{
            var frames = page.frames();
            let detect = 0
            // console.log(frames.length);
            for (let frame=0; frame<frames.length; frame++){
                if (frames[frame].url() === ""){
                    continue;
                }
                var pg_content = await frames[frame].content();

                pg_content = pg_content.toLowerCase();
                // var match = "";
                if (pg_content.includes('ad-blocker')){
                    match = 'ad-blocker';
                } else if (pg_content.includes('ad blocker')){
                    match = 'ad blocker';
                } else if (pg_content.includes(' adblocker ')){
                    match = ' adblocker ';
                } else if (pg_content.includes('adblock.detect')){
                    match = 'adblock.detect';
                }
                if (match !== ""){
                    const arr = pg_content.split(match)
                    let pgsrc1 = arr[0].substr(arr[0].length - 30)
                    let pgsrc2 = arr[1].slice(0,30)
                    let pgsrc = pgsrc1 + match + pgsrc2
                    
                    console.log(`adblocker_detected_in_frame: ${site} ${args[3]} ${pgsrc}`);
                    await page.screenshot({path: `ss/${args[3]}/${args[4]}.png`});
                    detect = 1;
                    break;
                }
            }
            if (detect === 1){
                break;
            }
        }
    }

    await browser.close();
    xvfb.stop();
})();

