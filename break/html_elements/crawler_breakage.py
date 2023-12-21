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
import os
import subprocess
from pyvirtualdisplay import Display
import sys
import random

def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]

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
        print('popup', 1, e)

    close_button.extend(close_anchor)
    if len(close_button) > 0:
        for i in close_button:
            try:
                # print(i.text)
                i.click()

            except Exception as e:
                print(i.text)
                print('popup', 2, e)

# could possibly make the driver stale. plz check!
def remove_alert(driver):
    alert = ''
    # Alert
    try:
        # Wait for the alert to be present
        WebDriverWait(driver, 10).until(EC.alert_is_present())
    except Exception as e:
        print("No alert present.", 1, e)

    # Wait for the modal to be visible
    try: 
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(@class, 'modal') and contains(@role, 'dialog')]"))
        )
    except Exception as e:
        print('modal element not found', 2, e)

    if alert:
        try:
            # Switch to the alert
            alert = driver.switch_to.alert

            # You can also retrieve alert text if needed: alert_text = alert.text

            # Accept the alert (clicks "Ok")
            alert.accept()

            # If you need to dismiss the alert (clicks "Cancel"), use: alert.dismiss()
        except Exception as e:
            print("couldn't switch to alert", 3, e)

def remove_cmp_banner(options):
    options.add_extension(f'/home/ritik/work/pes/extensions/extn_crx/Consent-O-Matic.crx')
    return options
        
# this removes captcha and brings determinism
def use_catapult(options, fname):
    folder_path = f"/home/ritik/work/pes/measurements/break/html_elements/wpr_data/{fname}"
    if not os.path.exists(folder_path):
    # Create the folder
        os.makedirs(folder_path)
        
    options.add_argument('--ignore-certificate-errors')
    options.add_argument(folder_path)
    options.add_argument('--host-resolver-rules="MAP *:80 127.0.0.1:9090,MAP *:443 127.0.0.1:9091,EXCLUDE localhost')
    options.add_argument('--ignore-certificate-errors-spki-list=PhrPvGIaAMmd29hj8BCZOq096yj7uMpRNHpn5PDxI6I=,2HcXCSKKJS0lEXLQEWhpHUfGuojiU0tiT5gOF9LP6IQ=')
    return options

        
extn_lst = [
     'control'
    #  , 'adblock', 'ublock', 'privacy-badger',
    #     "ghostery",
    #     "adguard"
    ]

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
        options.add_extension(f'/home/ritik/work/pes/measurements/extensions/extn_crx/{extn}.crx')

    vdisplay = Display(visible=False, size=(1920, 1280))
    vdisplay.start()

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
                print('ghostery', 1, e)
                return

    driver.get(site)
    wait_until_loaded(driver)
    time.sleep(2)

    remove_popup(driver)
    remove_alert(driver) # optional

    curr_scroll_position = -1
    curr_time = time.time()
    while True:
        # Define the scroll step size
        scroll_step = 50  # Adjust this value to control the scroll speed
        # Get the current scroll position
        scroll_position = driver.execute_script("return window.pageYOffset;")
        # Check if we've reached the bottom
        if curr_scroll_position == scroll_position:
            break
        else:
            curr_scroll_position = scroll_position

        # Scroll down by the step size
        driver.execute_script(f"window.scrollBy(0, {scroll_step});")
        
        # Wait for a bit (this controls the scroll speed indirectly)
        time.sleep(0.1)  # Adjust this value to control the scroll speed
        if time.time() - curr_time >= 45:
            break

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

    driver.quit()
    vdisplay.stop()

if __name__ == "__main__":
    # Parse the command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--replay', type=int)
    if len(sys.argv) < 2:
        parser.print_help(sys.stderr)
        sys.exit(1)
    args = parser.parse_args()
                  
    try:
        with open("../../break/adblock_detect/inner_pages_custom_break.json", "r") as f:
            updated_dict = json.load(f)
        f.close()

        # filtering the landing pages
        websites = []
        for key in updated_dict:
            websites.append(updated_dict[key][0])
        
        websites = random.sample(websites, 150)
        with open('manual_analysis.txt', 'w') as f:
            for site in websites:
                f.write(site)
                f.write('\n')
        f.close()
        # for i in range(len(websites)):
        #     websites[i] = 'https://' + websites[i].split('://')[1]
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
        print(len(websites), websites)

        chunks_list = list(divide_chunks(websites, SIZE))
        
        # multiprocess
        manager = multiprocessing.Manager()
        return_dict = manager.dict()
        result_dict = {}
        for extn in extn_lst:
            folder_path = f'/home/ritik/work/pes/measurements/break/html_elements/wpr_data/{extn}'
            if not os.path.exists(folder_path):
            # Create the folder
                os.makedirs(folder_path)

            original_directory = os.getcwd()
            target_directory = '/home/ritik/go/src/github.com/catapult-project/catapult/web_page_replay_go/'

            # Change to the target directory
            os.chdir(target_directory)

            if args.replay == 0:
                try:
                    cmd = ['go', 'run', 'src/wpr.go', 'record', '--http_port=9090', '--https_port=9091', f'/home/ritik/work/pes/measurements/break/html_elements/archive/{extn}.wprgo']

                    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)#, timeout = 180)

                except subprocess.TimeoutExpired as t:
                    print(f'Timeout for site: {site} {extn}')
                    sys.exit(0)
                except subprocess.CalledProcessError as e:
                    print(f'Error for site: {site} {extn}')
                    sys.exit(0)

                except Exception as e:
                    print(e)
                    sys.exit(0)

            elif args.replay == 1:
                try:
                    cmd = ['go', 'run', 'src/wpr.go', 'replay', '--http_port=9090', '--https_port=9091', f'/home/ritik/work/pes/measurements/break/html_elements/archive/{extn}.wprgo']

                    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)#, timeout = 180)

                except subprocess.TimeoutExpired as t:
                    print(f'Timeout for site: {site} {extn}')
                    sys.exit(0)
                except subprocess.CalledProcessError as e:
                    print(f'Error for site: {site} {extn}')
                    sys.exit(0)

                except Exception as e:
                    print(e)
                    sys.exit(0)
            
            else:
                print('Proceeding with no record-replay')


            os.chdir(original_directory)
            
            time.sleep(5) # wait for proxy to start

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

            # process.terminate()
            time.sleep(2) # time for port to be available again

    except KeyboardInterrupt:
        print('KeyboardInterrupt', 'Interrupted')

        if args.replay:
            f = open('html_breakages.json', 'w')
            json.dump(result_dict, f)
            f.close()

        try:
            # process.terminate()
            sys.exit(130)
        except SystemExit:
            os._exit(130)

    except Exception:
        print('Interrupted')

        if args.replay:
            f = open('html_breakages.json', 'w')
            json.dump(result_dict, f)
            f.close()

        try:
            # process.terminate()
            sys.exit(130)
        except SystemExit:
            os._exit(130)