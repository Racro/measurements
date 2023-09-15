const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({
    headless: false,
    defaultViewport: null,
    args: ['--window-size=1000,800']
  });
  const page = await browser.newPage();
  await page.goto('https://www.facebook.com', { waitUntil: 'networkidle2', timeout: 60000 });

  await scrollToBottom(page);
  await page.waitForTimeout(3000);

  await browser.close();
})();

async function scrollToBottom(page) {
  const distance = 100; // should be less than or equal to window.innerHeight
  const delay = 100;
  while (await page.evaluate(() => document.scrollingElement.scrollTop + window.innerHeight < document.scrollingElement.scrollHeight)) {
    await page.evaluate((y) => { document.scrollingElement.scrollBy(0, y); }, distance);
    await page.waitForTimeout(delay);
  }
}