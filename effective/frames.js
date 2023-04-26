const puppeteer = require('puppeteer')
const Xvfb = require('xvfb');

var args = process.argv; // node iframes.js site extn

(async () => {
    var xvfb = new Xvfb({
        silent: true,
        xvfb_args: ["-screen", "0", '1280x720x24', "-ac"],
    });
    xvfb.start((err)=>{if (err) console.error(err)})
    const browser = await puppeteer.launch({
        headless: false,
        ignoreDefaultArgs: ["--disable-extensions","--enable-automation"],
        defaultViewport: null, //otherwise it defaults to 800x600
        args: ['--no-sandbox', 
        '--start-fullscreen',            
        '--display='+xvfb._display,
        `--load-extension=/home/ritik/work/pes/extensions/privacy_extn/${args[3]}`
        ]
        });
    const page = await browser.newPage();
    await page.setViewport({ width: 1920, height: 1080 });
    await page.waitForTimeout(10000);
    await page.goto(args[2], {waitUntil: 'networkidle2'});
    await page.waitForTimeout(2000);

    const metrics = await page.metrics();
    console.log(metrics);
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