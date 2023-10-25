import asyncio
from selenium import webdriver
from selenium.webdriver.common.bidi.cdp import CdpSession
from selenium.webdriver.chrome.options import Options
import time

def create_cdp_session(driver):
    # Fetch list of all available targets
    targets = driver.execute_cdp_cmd('Target.getTargets', {})
    
    # print(targets)
    # Find the target that corresponds to our Selenium-driven browser session
    target_id = next(target['targetId'] for target in targets['targetInfos'] if target['type'] == 'page')
    
    # Create a CDP session using this target
    session = driver.execute_cdp_cmd('Target.attachToTarget', {'targetId': target_id, 'flatten': True})
    session_id = session['sessionId']

    return session_id, target_id

def get_lcp(driver, session_id, target_id):
    # Enable necessary events to monitor performance metrics
    driver.execute_cdp_cmd("Performance.enable", {})
    driver.execute_cdp_cmd("Page.enable", {})

    # Navigate to the website
    driver.get('https://www.rakuten.co.jp')
    
    # Let's give the page some time to load and stabilize the metrics
    # time.sleep(5)

    # Retrieve performance metrics from CDP
    # metrics = driver.execute_cdp_cmd("Performance.getTimeline", {})
    time.sleep(2)

    # Step 1: Inject the script to set up PerformanceObserver
    driver.execute_script('''
        window.lcpRenderTime = null;  // Create a global variable to store the render time
        
        new PerformanceObserver(entryList => {
            window.lcpRenderTime = entryList.getEntries()[0].renderTime;
        }).observe({ type: 'largest-contentful-paint', buffered: true });
    ''')

    # Step 2: Continuously poll to check if the global variable is set
    timeout = 10  # maximum time (in seconds) you're willing to wait for LCP
    end_time = time.time() + timeout
    while time.time() < end_time:
        renderTime = driver.execute_script('return window.lcpRenderTime;')
        if renderTime is not None:
            break
        time.sleep(0.5)  # wait for half a second before checking again

    print(f"LCP Render Time: {renderTime}")
    return renderTime

def main():
    global driver

    # Initialize Selenium
    options = Options()
    options.binary_location = "/home/ritik/work/pes/chrome_113/chrome"
    options.add_extension('/home/ritik/work/pes/extensions/extn_crx/ublock.crx')

    driver = webdriver.Chrome(options=options)

    session_id, target_id = create_cdp_session(driver)
    lcp = get_lcp(driver, session_id, target_id)

    if lcp:
        print(f"LCP Value: {lcp}ms")
    else:
        print("Couldn't fetch LCP.")

    driver.quit()

if __name__ == "__main__":
    main()
