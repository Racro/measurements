from browsermobproxy import Server
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
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

from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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


# Initialize BrowserMob Proxy
server = Server("/home/ritik/work/pes/browsermob-proxy/bin/browsermob-proxy")
server.start()
proxy = server.create_proxy()

def main(num_tries, args_lst):
    # Start X
    data_usage = []
    vdisplay = Display(visible=False, size=(1920, 1080))
    vdisplay.start()

    # Initialize Selenium
    options = Options()
    # options.add_argument('headless=new')
    options.add_argument('ignore-certificate-errors')
    options.add_argument("--proxy-server={0}".format(proxy.proxy))
    options.add_argument("no-sandbox")
    options.add_argument("--disable-animations")
    options.add_argument("--disable-web-animations")
    # options.add_argument("--single-process")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-web-security")
    options.add_argument("--disable-features=IsolateOrigins,site-per-process")
    options.add_argument("--disable-features=AudioServiceOutOfProcess")
    options.add_argument("auto-open-devtools-for-tabs")
    options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36") 
    #options.add_extension("/home/seluser/measure/harexporttrigger-0.6.3.crx")
    options.binary_location = "/home/seluser/measure/chrome_113/chrome"
    # options.binary_location = "/home/ritik/work/pes/chrome_113/chrome"
    if args_lst[-1] != "":
        options.add_extension(args_lst[-1])


    for i in range(num_tries):
        # Launch Chrome and install our extension for getting HARs
        driver = webdriver.Chrome(options=options)
        driver.set_page_load_timeout(args_lst[1])
        time.sleep(10)

        try:
            # Create a new HAR with the following options
            proxy.new_har("example", options={'captureHeaders': True, 'captureContent': True})

            # Use Selenium to navigate to a webpage
            driver.get("http://www.forbes.com")
            wait_until_loaded(driver, args_lst[1])

            # Collect HAR data
            result = proxy.har

            # Analyze HAR data (this is a simplified example)
            total_size = 0
            for entry in result['log']['entries']:
                # print(entry['response'])
                total_size += entry['response']['bodySize']
            # print(len(result['log']['entries']))
            # print(f"Total data usage: {total_size} bytes")
            data_usage.append(total_size)
        except Exception as e:
            print(e)

        # Stop Selenium and BrowserMob Proxy
        driver.quit()
    
    vdisplay.stop()
    return data_usage

if __name__ == '__main__':
    # Parse the command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('website')
    parser.add_argument('--timeout', type=int, default=60)
    # parser.add_argument('--extensions')
    parser.add_argument('--extensions-wait', type=int, default=10)
    args = parser.parse_args()

    fname = '/data/' + args[0].split('//')[1]
    extn = fname
    args_lst = [args.website, args.timeout]

    # calibrate
    # for i in range(3):
    #     main(3, 1, args_lst)

    data_dict = {}
    extensions_path = pathlib.Path("/home/seluser/measure/extensions/extn_crx")
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
                    print(f"{args_lst[-1]} - Extension not found")
                    sys.exit(1)

        ret = main(3, new_args)

        if extn == "":
            data_dict[fname] = ret
        else:
            data_dict[extn] = ret
    
    with open(fname, 'w') as f:
        json.dump(data_dict, f)
    f.close()

    server.stop()