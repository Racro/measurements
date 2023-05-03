const puppeteer = require('puppeteer')
// const fs = require('fs-extra')

// const filePath = 'datausage.csv'
const Xvfb = require('xvfb');
const fakeUA  = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36';
var args = process.argv; // node content.js site extn

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
            "--disable-dev-shm-usage",
            "--no-sandbox",
            '--disable-web-security',
            '--disable-features=IsolateOrigins,site-per-process',
            // `--load-extension=/home/ritik/work/pes/extensions/privacy_extn/${args[3]}`,
            '--display='+xvfb._display,
            '--window-size=960, 1080',
            '--disable-features=AudioServiceOutOfProcess'
	    // '--user-agent="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0"'
        ];
    }
    else{
        p_args= [
            "--disable-gpu",
            "--disable-dev-shm-usage",
            "--no-sandbox",
            '--disable-web-security',
            '--disable-features=IsolateOrigins,site-per-process',
            `--load-extension=./../../extensions/extn_src/${args[3]}`,
            '--display='+xvfb._display,
            '--window-size=960, 1080',
            '--disable-features=AudioServiceOutOfProcess'
	    // '--user-agent="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0"'
        ];
    }
    const browser = await puppeteer.launch({
        headless: false,
        // headless: "new",
        ignoreDefaultArgs: ["--disable-extensions","--enable-automation"],
        args: p_args,
        executablePath: '/usr/bin/google-chrome' 
        // executablePath: '/snap/bin/chromium' 
    });
    const page = await browser.newPage();
    await page.setViewport({ width: 960, height: 1080 });
    await page.setUserAgent(fakeUA);
    await page.waitForTimeout(10000);
    var sites = args[2].split(',');
    
    let Bytes = 0;
    // Set Request Interception to detect images, fonts, media, and others
    page.setRequestInterception(true);

    page.on('request', request => {
        request.continue();
    });

    page.on('response', response => {
        let headers = response.headers();
        // console.log(headers['content-length'])
        if ( typeof headers['content-length'] !== 'undefined' ){
            const length = parseInt( headers['content-length'] );
            // console.log(Bytes);
            Bytes+= length;
        }
    });

    var totalBytes = 0; 
    var num_sites = 0;
    // Navigate to page
    // await page.goto('https://www.google.com', {waitUntil: 'networkidle0', timeout: 60000})
    for (let index=0; index<sites.length; index++){
        let site = sites[index];
        try{
            await page.goto(site, { waitUntil: 'networkidle2', timeout: 60000 });
        } catch (error){
            console.error(error);
            console.error(site);
            // continue;
            break;
        }
        await page.waitForTimeout(2000);
        // console.log(Bytes);
        num_sites += 1;
        totalBytes += Bytes;
    }

    if (num_sites != 0){
        console.log(`Total_data_used_by_site ${sites[0]}: ${totalBytes/(1048576*num_sites)} MBytes`);
    }

    await browser.close();
    xvfb.stop();
})();
