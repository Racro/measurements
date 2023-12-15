from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.chrome.service import Service

import time 

def is_loaded(webdriver):
    return webdriver.execute_script("return document.readyState") == "complete"

def wait_until_loaded(webdriver, timeout=60, period=0.25, min_time=0):
    start_time = time.time()
    mustend = time.time() + timeout
    while time.time() < mustend:
        if is_loaded(webdriver):
            if time.time() - start_time < min_time:
                time.sleep(min_time + start_time - time.time())
            return True
        time.sleep(period)
    return False

# Prepare Chrome
options = Options()
#options.headless = False
# options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-animations")
options.add_argument("--disable-web-animations")
# options.add_argument("--incognito")
# options.add_argument("--single-process")
options.add_argument("--disable-gpu")
options.add_argument("--disable-features=IsolateOrigins,site-per-process")
options.add_argument("--disable-features=AudioServiceOutOfProcess")
# options.add_argument("auto-open-devtools-for-tabs")
options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36")

# options.add_argument("--user-data-dir=/home/ritik/wpr_data")
# options.add_argument('--host-resolver-rules="MAP *:80 127.0.0.1:9090,MAP *:443 127.0.0.1:9091,EXCLUDE localhost')
# options.add_argument('--ignore-certificate-errors-spki-list=PhrPvGIaAMmd29hj8BCZOq096yj7uMpRNHpn5PDxI6I=,2HcXCSKKJS0lEXLQEWhpHUfGuojiU0tiT5gOF9LP6IQ=')


#options.add_extension("/home/seluser/measure/harexporttrigger-0.6.3.crx")
# options.add_extension(f'/home/ritik/work/pes/extensions/extn_crx/Consent-O-Matic.crx')
# options.add_extension(f'/home/ritik/work/pes/measurements/extensions/extn_crx/adblock.crx')
options.binary_location = "/home/ritik/work/pes/chrome_113/chrome"
# service = Service(executable_path='/usr/local/bin/chromedriver')

sites = [
    'https://www.mrdonn.org'
    # 'https://www.forbes.com'
    # 'https://www.geeksforgeeks.org/data-structures/?ref=shm_outind'
    #      'https://www.wayfair.com'
    #      , 'https://www.godaddy.com', 
        #  'https://www.groupon.com',
        # 'https://www.wayfair.com',
        # 'https://www.wayfair.com',
        # 'https://www.wayfair.com',
        # 'https://www.wayfair.com',
        # 'https://www.wayfair.com'
]

for site in sites:
    driver = webdriver.Chrome(options=options)
    # time.sleep(15)
    driver.get(site)
    wait_until_loaded(driver)
    time.sleep(5)
    driver.get(site)

    
        
    # close_button = []
    # close_anchor = []
    # # Find the close button (this uses a common convention of 'x' or 'close' text)
    # try:
    #     close_button = driver.find_elements(By.XPATH, "//button[contains(translate(., 'CLOSE', 'close'), 'close') or contains(translate(@aria-label, 'CLOSE', 'close'), 'close')]")
    #     close_anchor = driver.find_elements(By.XPATH, "//a[contains(translate(., 'CLOSE', 'close'), 'close') or contains(translate(@aria-label, 'CLOSE', 'close'), 'close')]")
    # except Exception as e:
    #     print(close_button, close_anchor)
    #     print(1, e)

    # close_button.extend(close_anchor)
    # if len(close_button) > 0:
    #     for i in close_button:
    #         try:
    #             print(i.text)
    #             # i.click()

    #         except Exception as e:
    #             print(i)
    #             print(2, e)
    
    
    # alert = ''
    # # Alert
    # try:
    #     # Wait for the alert to be present
    #     WebDriverWait(driver, 10).until(EC.alert_is_present())
    # except Exception as e:
    #     print("No alert present.", e)

    # # Wait for the modal to be visible
    # try: 
    #     WebDriverWait(driver, 10).until(
    #         EC.visibility_of_element_located((By.XPATH, "//*[contains(@class, 'modal') and contains(@role, 'dialog')]"))
    #     )
    # except Exception as e:
    #     print(e)
    #     print('modal element not found')

    # if alert:
    #     try:
    #         # Switch to the alert
    #         alert = driver.switch_to.alert

    #         # You can also retrieve alert text if needed: alert_text = alert.text

    #         # Accept the alert (clicks "Ok")
    #         alert.accept()

    #         # If you need to dismiss the alert (clicks "Cancel"), use: alert.dismiss()
    #     except Exception as e:
    #         print(e)
    #         print("couldn't switch to alert")
    
    time.sleep(25)

    driver.quit()