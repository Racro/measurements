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
    // xvfb.start((err)=>{if (err) console.error(err)});

    const browser = await puppeteer.launch({ 
        headless: false,
        ignoreDefaultArgs: ["--disable-extensions","--enable-automation"],
        args: [
            "--disable-gpu",
            "--disable-dev-shm-usage",
            "--no-sandbox",
            // "--disable-setuid-sandbox",
            // "--no-first-run",
            // "--no-zygote",
            // "--single-process",
            '--disable-web-security',
            '--disable-features=IsolateOrigins,site-per-process',
            // `--load-extension=/home/ritik/work/pes/extensions/privacy_extn/${args[3]}`,
            // '--display='+xvfb._display,
            // '--single-process',
            '--window-size=960,1080',
            '--disable-features=AudioServiceOutOfProcess'
        ],
        // executablePath: '/usr/bin/google-chrome' 
        executablePath: '/snap/bin/chromium' 
    });
    const page = await browser.newPage();
    await page.setViewport({ width: 960, height: 1080 });
    await page.waitForTimeout(2000);
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
        
        // let source = await page.content();
        // source = source.toLowerCase();
        // if (source.includes('ad-blocker') || source.includes('ad blocker')){
        //     await page.screenshot({path: `ss/${args[3]}/${args[4]}.png`});
        //     console.log(`adblocker_detected: ${site} ${args[3]}`);
        //     break;
        // }
        // else{
        //     var frames = page.frames();
        //     let detect = 0
        //     // console.log(frames.length);
        //     for (let frame=0; frame<frames.length; frame++){
        //     // for (let frame=2; frame<3; frame++){
        //         // console.log(frame);
        //         // console.log(frames[frame].src);
        //         // console.log(frames[frame].url());
        //         if (frames[frame].url() === ""){
        //             continue;
        //         }
        //         var pg_content = await frames[frame].content();
        //         // if (frame === 41){
        //         //     console.log(pg_content);
        //         // }
        //         pg_content = pg_content.toLowerCase();
        //         // console.log(pg_content);
        //         // console.log("-------------------------------------");

        //         if (pg_content.includes('ad-blocker') || pg_content.includes('ad blocker')){
        //             console.log(`adblocker_detected_in_frame: ${site} ${args[3]}`);
        //             await page.screenshot({path: `ss/${args[3]}/${args[4]}.png`});
        //             detect = 1;
        //             break;
        //         }
        //     }
        //     if (detect === 1){
        //         break;
        //     }
        // }
    }

    await browser.close();
    // xvfb.stop();
})();

