from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException

import time 
import multiprocessing
import json
import argparse

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

def remove_popup(driver):
    close_button = []
    close_anchor = []
    # Find the close button (this uses a common convention of 'x' or 'close' text)
    try:
        close_button = driver.find_elements(By.XPATH, "//button[contains(translate(., 'CLOSE', 'close'), 'close') or contains(translate(@aria-label, 'CLOSE', 'close'), 'close')]")
        close_anchor = driver.find_elements(By.XPATH, "//a[contains(translate(., 'CLOSE', 'close'), 'close') or contains(translate(@aria-label, 'CLOSE', 'close'), 'close')]")
    except Exception as e:
        # print(close_button, close_anchor)
        print(1, e)

    close_button.extend(close_anchor)
    if len(close_button) > 0:
        for i in close_button:
            try:
                # print(i.text)
                i.click()

            except Exception as e:
                print(i.text)
                print(2, e)

# could possibly make the driver stale. plz check!
def remove_alert(driver):
    alert = ''
    # Alert
    try:
        # Wait for the alert to be present
        WebDriverWait(driver, 10).until(EC.alert_is_present())
    except Exception as e:
        print("No alert present.", e)

    # Wait for the modal to be visible
    try: 
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(@class, 'modal') and contains(@role, 'dialog')]"))
        )
    except Exception as e:
        print(e)
        print('modal element not found')

    if alert:
        try:
            # Switch to the alert
            alert = driver.switch_to.alert

            # You can also retrieve alert text if needed: alert_text = alert.text

            # Accept the alert (clicks "Ok")
            alert.accept()

            # If you need to dismiss the alert (clicks "Cancel"), use: alert.dismiss()
        except Exception as e:
            print(e)
            print("couldn't switch to alert")

def remove_cmp_banner(options):
    options.add_extension(options.add_extension(f'/home/ritik/work/pes/extensions/extn_crx/Consent-O-Matic.crx'))
    return options
        
# this removes captcha and brings determinism
def use_catapult(options, fname):
    options.add_argument(f"--user-data-dir=/home/ritik/wpr_data_{fname}")
    options.add_argument('--host-resolver-rules="MAP *:80 127.0.0.1:9090,MAP *:443 127.0.0.1:9091,EXCLUDE localhost')
    options.add_argument('--ignore-certificate-errors-spki-list=PhrPvGIaAMmd29hj8BCZOq096yj7uMpRNHpn5PDxI6I=,2HcXCSKKJS0lEXLQEWhpHUfGuojiU0tiT5gOF9LP6IQ=')
    return options

        
extn_lst = [
     'control', 'adblock', 'ublock', 'privacy-badger',
        "decentraleyes",
        "disconnect",
        "ghostery",
        "adguard"]

SIZE = 15 # number of browser windows that will open

def run(site, extn, return_dict, l, replay):
    # Prepare Chrome
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-animations")
    options.add_argument("--disable-web-animations")
    options.add_argument("--disable-gpu")

    options.add_argument("--disable-features=IsolateOrigins,site-per-process")
    options.add_argument("--disable-features=AudioServiceOutOfProcess")
    options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36")
    options.binary_location = "/home/ritik/work/pes/chrome_113/chrome"
            
    options = remove_cmp_banner(options)
    options = use_catapult(options, extn)

    if extn != 'control':
        options.add_extension(f'/home/ritik/work/pes/extensions/extn_crx/{extn}.crx')
            
    driver = webdriver.Chrome(options=options)
    time.sleep(2) # wait for extension to load

    if extn == 'adblock':
        time.sleep(15)
    elif extn == 'ghostery':
        windows = driver.window_handles
        for window in windows:
            try:
                driver.switch_to.window(window)
                url_start = driver.current_url[:16]
                if url_start == 'chrome-extension':
                    element = driver.find_element(By.XPATH, "//ui-button[@type='success']")
                    element.click()
                    time.sleep(2)
                    break
            except Exception as e:
                continue

    driver.get(site)
    wait_until_loaded(driver)
    time.sleep(2)
        
    remove_popup(driver)
    remove_alert(driver) # optional

    if replay:
            
        breakages = [] # list of breakages found
        
        # function to test breakages
        
        
        try:
            l.acquire()
            # print(fname)
            return_dict[extn][site].extend([breakages])
            l.release()
        except Exception as e:
            print(e)
            l.release()

if __name__ == "__main__":
    # Parse the command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--replay', type=int, default=1)
    args = parser.parse_args()
                  
    try:
        with open("../../break/adblock_detect/inner_pages_custom.json", "r") as f:
            updated_dict = json.load(f)
        f.close()

        # filtering the landing pages
        websites = []
        for key in updated_dict:
            websites.append(updated_dict[key][0])
        # sites = [
        # # 'https://www.forbes.com'
        #     'https://www.spirit.com'
        # #      'https://www.wayfair.com'
        # #      , 'https://www.godaddy.com', 
        #     #  'https://www.groupon.com',
        #     # 'https://www.wayfair.com',
        #     # 'https://www.wayfair.com',
        #     # 'https://www.wayfair.com',
        #     # 'https://www.wayfair.com',
        #     # 'https://www.wayfair.com'
        #     ]        


        # deciding on the number of workers
        # latest_list = list(updated_dict.keys())
        print(len(websites))
        chunks_list = list(divide_chunks(websites, SIZE))
        
        # multiprocess
        manager = multiprocessing.Manager()
        return_dict = manager.dict()
        result_dict = {}
        for extn in extn_lst:       
            return_dict[extn] = manager.dict()
            result_dict[extn] = {}
            for i in range(len(chunks_list)):
                jobs = []
                for site in chunks_list[i]:
                    return_dict[extn][site] = manager.list()
                    result_dict[extn][site] = []
                    p = multiprocessing.Process(target=run, args=(site, extn, return_dict, multiprocessing.Lock(), args.replay, ))
                    jobs.append(p)
                for job in jobs:
                    job.start()
                for job in jobs:
                    job.join()
                
            if args.replay:                
                for site in websites:
                    print(return_dict[extn][site])
                    for val in return_dict[extn][site]:
                        result_dict[extn][site].append(val)

                f = open('html_breakages.json', 'w')
                json.dump(result_dict, f)
                f.close()

    except KeyboardInterrupt:
        print('Interrupted')

        if args.replay:
            f = open('html_breakages.json', 'w')
            json.dump(result_dict, f)
            f.close()

        try:
            sys.exit(130)
        except SystemExit:
            os._exit(130)

    except Exception:
        print('Interrupted')

        if args.replay:
            f = open('html_breakages.json', 'w')
            json.dump(result_dict, f)
            f.close()