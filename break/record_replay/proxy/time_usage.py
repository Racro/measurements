from urllib.parse import urlparse

import requests
from browsermobproxy import Server
import tldextract
import time
from adblockparser import *
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
import multiprocessing
import random
import signal

from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

start_time = time.time()

# from functions import *

def write_JSON(name, my_dict):
    json_file_path = 'json_time/' + name + ".json"
    with open(json_file_path, "w") as json_file:
        json.dump(my_dict, json_file)
    json_file.close()

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
    
def webStats(webdriver):
    try:
        navigationStart = webdriver.execute_script("return window.performance.timing.navigationStart")
        # responseStart = webdriver.execute_script("return window.performance.timing.responseStart")
        domComplete = webdriver.execute_script("return window.performance.timing.domComplete")
        loadEnd = webdriver.execute_script("return window.performance.timing.loadEventEnd")
    except Exception as e:
        print(e)
        return -1, -1
    
    return domComplete - navigationStart, loadEnd - navigationStart

def main(num_tries, args_lst, display_num, extn, store_data):
   
    # display number
    os.environ['DISPLAY'] = f":{display_num}"
    
    # Initialize Selenium
    options = Options()
    # options.add_argument("start-maximized")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-animations")
    options.add_argument("--disable-web-animations")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-features=IsolateOrigins,site-per-process")
    options.add_argument("--disable-features=AudioServiceOutOfProcess")
  
    options.add_argument(
        "--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36")

    options.binary_location = "/home/ritik/work/pes/chrome_113/chrome"
    # if args_lst[-1] != "":
    #     options.add_extension(args_lst[-1])

    driver = ''
    data = []
    website = args_lst[0]
    key = ''
    if 'http' in website:
        key = website.split('http://')[1]
    if 'www' in key:
        key = key.split('www.')[1]

    a = [] #1
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(args_lst[1])
    time.sleep(2)
    try:
        for i in range(6):
            # Launch Chrome and install our extension for getting HARs
            try:
                print("website: ", website)
                driver.get(website)
                wait_until_loaded(driver, args_lst[1])
                time.sleep(2)
                domComplete, loadEnd  = webStats(driver)
                a.append((domComplete, loadEnd))
            except Exception as e:
                print(1, e)
                continue
            time.sleep(5)
        data.append(a)
        store_data[extn][key] = data

        # Stop Selenium and BrowserMob Proxy
        if driver != '':
            driver.quit()
            time.sleep(2)
    
    except Exception as e:
        print(11, e)

    a = [] #2
    if args_lst[-1] != "":
        options2 = options
        options2.add_extension(args_lst[-1])
    driver = webdriver.Chrome(options=options2)
    driver.set_page_load_timeout(args_lst[1])
    time.sleep(2)

    if extn == 'adblock':
        time.sleep(15)
    elif extn == 'ghostery':
        windows = self.driver.window_handles
        for window in windows:
            try:
                self.driver.switch_to.window(window)
                url_start = self.driver.current_url[:16]
                if url_start == 'chrome-extension':
                    element = self.driver.find_element(By.XPATH, "//ui-button[@type='success']")
                    element.click()
                    time.sleep(2)
                    break
            except Exception as e:
                print('ghostery', 1, e)
                return 0
    try:
        for i in range(5):
            # Launch Chrome and install our extension for getting HARs
            try:
                print("website: ", website)
                driver.get(website)
                wait_until_loaded(driver, args_lst[1])
                time.sleep(2)

                domComplete, loadEnd  = webStats(driver)
                a.append((domComplete, loadEnd))
            except Exception as e:
                print(2, e)
                continue
    
            time.sleep(5)
        data.append(a)
        store_data[extn][key] = data

        # Stop Selenium and BrowserMob Proxy
        if driver != '':
            driver.quit()
            time.sleep(2)
    
    except Exception as e:
        print(4, e)

    a = [] #3
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(args_lst[1])
    time.sleep(2)
    
    try:
        for i in range(5):
            # Launch Chrome and install our extension for getting HARs
            try:
                print("website: ", website)
                driver.get(website)
                wait_until_loaded(driver, args_lst[1])
                time.sleep(2)

                domComplete, loadEnd  = webStats(driver)
                a.append((domComplete, loadEnd))
            except Exception as e:
                print(3, e)
                continue
            
            time.sleep(5)
        data.append(a)
        store_data[extn][key] = data

        # Stop Selenium and BrowserMob Proxy
        if driver != '':
            driver.quit()
            time.sleep(2)
        
    except Exception as e:
        print(5, e)


    store_data[extn][key] = data

SIZE = 60
if __name__ == '__main__':
    # Parse the command line arguments
    parser = argparse.ArgumentParser()
    # parser.add_argument('website')
    parser.add_argument('--timeout', type=int, default=60)
    # parser.add_argument('--extensions')
    parser.add_argument('--extensions-wait', type=int, default=10)
    args = parser.parse_args()

    manager = multiprocessing.Manager()

    data_dict = {}
    extensions_path = "/home/ritik/work/pes/measurements/extensions/extn_crx/"

    extension = 0

    name = str(extension)

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
            # ret, contacted_urls = main(3, new_args, proxy)
            # if extn == "":
            #     data_dict[fname] = [ret, contacted_urls]
            # else:
            #     data_dict[extn] = [ret, contacted_urls]

    else:
        # extensions = ["ublock", "privacy-badger", "adblock"]
        extensions = ["adblock"]
        extensions_dictionary = manager.dict()

        url_data = json.load(open(f'json/ublock_diff.json', 'r'))
        websites = list(url_data.keys())
        websites = random.sample(websites, 1000)
        website_chunks = list(divide_chunks(websites, SIZE))

        print(website_chunks)
        # generates extensions dictionary with just the ad blocker extension names
        for extension in extensions:
            extensions_dictionary[extension] = manager.dict()
            
            if extension != "control":
                name = extensions_path + extension + ".crx"
            else:
                name = ""

            for chunk in website_chunks:
                # website = "http://" + website
                jobs = []
                vdisplay = Display(visible=False, size=(1920, 1280))
                vdisplay.start()
                display = vdisplay.display

                for i, website in enumerate(chunk):
                    try:
                        fname = './data/' + website.split('//')[1].split('/')[0]
                        extn = fname
                        args_lst = [website, args.timeout]
                        new_args = args_lst
                        new_args.append(name)

                        p = multiprocessing.Process(target=main, args=(1, new_args, display, extension, extensions_dictionary))
                        jobs.append(p)
                        # ret = main(1, new_args, proxy)

                        # filtered_val is LIST with all the filtered packets

                        # large dictionary with all the results of each website.
                        # this should be seperate for each extension.
                        # all_resources[website] = filter_packets(website, ret, blacklist, inverse_lookup, regular_lookup).copy()

                        # write_JSON(extension, all_resources)

                        # data_dict = unfiltered and contains all the packets
                        # data_dict[fname] = ret
                        # with open(fname, 'w') as f:
                        #     json.dump(ret, f)
                        # f.close()
                    except Exception as e:
                        print(e)
                        print(website)

                for job in jobs:
                    job.start()
                
                time.sleep(5)

                for job in jobs:
                    print(f"joining {job}")
                    job.join(timeout = 900)

                    if job.is_alive():
                        job.terminate()
                
                time.sleep(2)
                print("-"*50)
                print("closing open xvfb processes")
                vdisplay.stop()
                os.system('pkill Xvfb')
                print(os.system("ps aux | grep Xvfb | wc -l"))
                print("-"*50)

                time.sleep(5)

            save_dict = {}
            for site in extensions_dictionary[extension].keys():
                save_dict[site] = extensions_dictionary[extension][site]
            write_JSON(extension, save_dict)
            # extensions_dictionary[extension] = save_dict
            # all_resources = {}



    end_time = time.time()

    # Calculate the elapsed time
    elapsed_time = end_time - start_time

    print("Elapsed time:", elapsed_time, "seconds")
