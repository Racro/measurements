from browsermobproxy import Server
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

import argparse
import json
import pathlib
import shutil
import subprocess
import sys
import time
# import threading
import os
from datetime import datetime
import ast 

from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

extensions_configurations = [
    # No extensions
   "",
#    # Extensions on their own
    "adblock",
    "decentraleyes",
    "disconnect",
    "ghostery",
    "https",
    "noscript",
    "privacy-badger",
    "ublock",
    "scriptsafe",
    "canvas-antifp",
    "adguard",
    "user-agent"  
    # Combinations
#    "decentraleyes,privacy_badger,ublock_origin"
]

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

def main(num_tries, args_lst, proxy):
    # Start X
    data_usage = {}
    contacted_urls = []
    vdisplay = Display(visible=False, size=(1920, 1080))
    vdisplay.start()

    # Initialize Selenium
    options = Options()
    # options.add_argument('headless=new')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--proxy-server={0}".format(proxy.proxy))
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-animations")
    options.add_argument("--disable-web-animations")
    # options.add_argument("--single-process")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-web-security")
    options.add_argument("--disable-features=IsolateOrigins,site-per-process")
    options.add_argument("--disable-features=AudioServiceOutOfProcess")
    # options.add_argument("auto-open-devtools-for-tabs")
    options.add_argument("--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36") 
    options.add_extension("/home/ritik/work/pes/measurements/extensions/extn_crx/ublock.crx")
    options.binary_location = "/home/ritik/work/pes/chrome_113/chrome"
    # options.binary_location = "/usr/bin/google-chrome"
    # options.binary_location = "/home/ritik/work/pes/chrome_113/chrome"
    if args_lst[-1] != "":
        options.add_extension(args_lst[-1])

    # Initialize service
    service = Service(executable_path='/usr/local/bin/chromedriver')

    for i in range(num_tries):    
        try:
            # Launch Chrome and install our extension for getting HARs
            driver = webdriver.Chrome(service=service, options=options)
            driver.set_page_load_timeout(args_lst[1])
            time.sleep(5)
            
            # Create a new HAR with the following options
            proxy.new_har("example", options={'captureHeaders': True, 'captureContent': True})

            # Use Selenium to navigate to a webpage
            # valid = 0
            # i += 1
            print(website)
            driver.get(website)
            wait_until_loaded(driver, args_lst[1])

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
            # valid += 1

            # Collect HAR data
            result = proxy.har

            # Analyze HAR data (this is a simplified example)
            total_size = 0
            data_usage[i] = result['log']['entries']
            print(len(data_usage[i]))
        except Exception as e:
            print(e, args_lst[0], file=sys.stderr)

        # Stop Selenium and BrowserMob Proxy
        driver.quit()
        time.sleep(2)
    
    vdisplay.stop()
    return data_usage

if __name__ == '__main__':
    # Parse the command line arguments
    parser = argparse.ArgumentParser()
    # parser.add_argument('website')
    parser.add_argument('--timeout', type=int, default=60)
    # parser.add_argument('--extensions')
    parser.add_argument('--extensions-wait', type=int, default=10)
    args = parser.parse_args()

    # websites = ast.literal_eval(args.website)
    # websites = [args.website]
    
    website_dict = json.load(open('../../adblock_detect/inner_pages_custom.json', 'r'))
    websites = []
    for key in website_dict:
        websites.append(website_dict[key][0])
    websites = websites[:100]

    print(f'data --- {websites}')

    # Initialize BrowserMob Proxy
    server = Server("/home/ritik/work/pes/browsermob-proxy/bin/browsermob-proxy")
    server.start()
    proxy = server.create_proxy()

    data_dict = {}
    # extensions_path = pathlib.Path("/home/seluser/measure/extensions/extn_crx")

    extension = 0    
    if extension:
        for extn in extensions_configurations:
            new_args = args_lst
            new_args.append(extn)
            if extn != "":
                for extension in args_lst[-1].split(","):
                    matches = list(extensions_path.glob("{}*.crx".format(extension)))
                    if matches and len(matches) == 1:
                        new_args.append(str(matches[0]))
                        # options.add_extension(str(matches[0]))
                        # extn = extension
                    else:
                        print(f"{args_lst[-1]} - Extension not found", file=sys.stderr)
                        sys.exit(1)
            ret, contacted_urls = main(3, new_args, proxy)
            if extn == "":
                data_dict[fname] = [ret, contacted_urls]
            else:
                data_dict[extn] = [ret, contacted_urls]
    
    else:
        for website in websites:
            try:
                fname = './ublock/' + website.split('//')[1].split('/')[0]
                extn = fname
                args_lst = [website, args.timeout]
                new_args = args_lst
                new_args.append("")

                ret = main(5, new_args, proxy)
                data_dict[fname] = ret
                with open(fname, 'w') as f:
                    json.dump(ret, f)
                f.close()
            except Exception as e:
                print(e)
                print(website)

    # with open(fname, 'w') as f:
    #     json.dump(data_dict, f)
    # f.close()

    server.stop()
