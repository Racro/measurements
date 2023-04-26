const puppeteer = require('puppeteer')
const Xvfb = require('xvfb');


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
        '--load-extension=/home/ritik/work/pes/extensions/privacy_extn/adblock'
        ]
        });
    const page = await browser.newPage();
    await page.setViewport({ width: 1920, height: 1080 });
    await page.waitForTimeout(10000);
    await page.goto('http://forbes.com', {waitUntil: 'networkidle2'});
    await page.waitForTimeout(2000);

    const metrics = await page.metrics();
    console.log(metrics);

    const performanceTiming = JSON.parse(
        await page.evaluate(() => JSON.stringify(window.performance.timing.connectStart))
    );
    console.log('performanceTiming', performanceTiming)

    // await page.screenshot({path: 'result.png'});
    await browser.close()
    xvfb.stop();
})()