const puppeteer = require('puppeteer')
const Xvfb = require('xvfb');
const fakeUA  = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36';
var args = process.argv; // node iframes.js site extn

const delay = (milliseconds) => new Promise((resolve) => setTimeout(resolve, milliseconds));

(async () => {
    var xvfb = new Xvfb({
        silent: true,
        reuse: true,
        // xvfb_args: ["-screen", "0", '1280x720x24', "-ac"],
    });
    xvfb.start((err)=>{if (err) console.error(err)})
    let p_args;
    if (args[3] === 'control'){
        p_args = [
            "--disable-gpu",
            '--disable-features=IsolateOrigins,site-per-process',
            // `--load-extension=/home/ritik/work/pes/extensions/privacy_extn/${args[3]}`,
            '--display='+xvfb._display,
            '--window-size=1280, 720',
            '--disable-features=AudioServiceOutOfProcess'
	    // '--user-agent="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0"'
        ];
    }
    else{
        p_args= [
            "--disable-gpu",
            '--disable-features=IsolateOrigins,site-per-process',
            `--disable-extensions-except=./../../extensions/extn_src/${args[3]}`,
            `--load-extension=./../../extensions/extn_src/${args[3]}`,
            '--display='+xvfb._display,
            '--window-size=1280, 720',
            '--disable-features=AudioServiceOutOfProcess'
	    // '--user-agent="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0"'
        ];
    }
    
    const browser = await puppeteer.launch({
        headless: false,
        // headless: "new",
        // ignoreDefaultArgs: ["--disable-extensions","--enable-automation"],
        args: p_args,
        executablePath: './../../../chrome_113/chrome' 
        // executablePath: '/snap/bin/chromium' 
    });

    await delay(3000);

    if ( args[3] == 'adblock' ){
        await delay(15000);    
    }
    else if ( args[3] == 'ghostery' ){
        let pages = await browser.pages();
        for(let i = 0; i < pages.length; i += 1) {
            if(pages[i].url().startsWith('chrome-extension://')) {
                try{
                    pages[i].click('xpath=//ui-button[@type="success"]');
                    break;
                }
                catch (e){
                    console.error(e);
                    console.error(args[3]);

                }
                
            }
        }
    }
    
    await delay(3000);

    var num_sites = 0;
    var frames = 0;
    var docs = 0;

    var sites = args[2].split(',');

    for (let index=0; index<sites.length; index++){ // sites.length
    // for (let index=0; index<1; index++){
        var page = await browser.newPage();
        // await page.setViewport({ width: 960, height: 1080 });
        await page.setUserAgent(fakeUA);
        let site = sites[index];
        
        try{
            await page.goto(site, { waitUntil: 'networkidle2', timeout: 60000 });
            await page.waitForTimeout(2000);
            var metrics = await page.metrics();
            frames += metrics[ 'Frames' ];
            docs += metrics[ 'Documents' ];
            num_sites += 1;
        } catch (error){
            console.error(error);
            console.error(site);
            continue;
            // break;
        }
        
    }
   
    if (num_sites != 0){
        console.log(`Total_frames_and_docs_for ${sites[0]}: ${frames/(num_sites)} ${docs/(num_sites)}`);
    } 

    // await page.screenshot({path: 'result.png'});
    await browser.close()
    await xvfb.stop();

    // const metrics = await page.metrics();
    // console.log(metrics);
    // {
    //     Timestamp: 270012.882634,
    //     Documents: 33,
    //     Frames: 65,
    //     JSEventListeners: 1345,
    //     Nodes: 2769,
    //     LayoutCount: 51,
    //     RecalcStyleCount: 80,
    //     LayoutDuration: 0.080674,
    //     RecalcStyleDuration: 0.026484,
    //     ScriptDuration: 0.836924,
    //     TaskDuration: 1.293764,
    //     JSHeapUsedSize: 30683564,
    //     JSHeapTotalSize: 55947264
    //   }

})();
