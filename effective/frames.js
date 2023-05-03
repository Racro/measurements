const puppeteer = require('puppeteer')
const Xvfb = require('xvfb');
const fakeUA  = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36';
var args = process.argv; // node iframes.js site extn

(async () => {
    var xvfb = new Xvfb({
        silent: true,
        xvfb_args: ["-screen", "0", '1280x720x24', "-ac"],
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
            `--load-extension=./../extensions/extn_src/${args[3]}`,
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
   
    var num_sites = 0;
    var frames = 0;
    var docs = 0;

    for (let index=0; index<sites.length; index++){
    // for (let index=0; index<1; index++){
        let site = sites[index];
        try{
            await page.goto(site, { waitUntil: 'networkidle2', timeout: 60000 });
            await page.waitForTimeout(2000);
        } catch (error){
            console.error(error);
            console.log(site);
            continue;
            // break;
        }
	
	const metrics = await page.metrics();
	frames += metrics[ 'Frames' ]
	docs += metrics[ 'Documents' ]
	num_sites += 1;
    }
   
    if (num_sites != 0){
        console.log(`Total_frames_and_docs_for ${sites[0]}: ${frames/(num_sites)} ${docs/(num_sites)}`);
    }





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
      

    // await page.screenshot({path: 'result.png'});
    await browser.close()
    xvfb.stop();
})()
