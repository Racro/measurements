#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import json
import sys
import time
import threading
import pathlib

from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def check_for_extn_installation(driver, name):  #generates a screenshot to check for extension installation
    driver.get("https://chrome.google.com/webstore/detail/adblock-plus-free-ad-bloc/cfhdojbkjhnklbpkdaibdccddilifddb")
    #save screenshot
    S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
    driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment
    file_name = name + '.png'
    driver.find_element(by=By.TAG_NAME, value='body').screenshot(file_name)

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

def find_all_iframes(driver):
    iframes = driver.find_elements(By.XPATH, value="//iframe")
    print(driver.current_url)
    print(len(iframes))
    i = 0
    for iframe in iframes:
        driver.switch_to.frame(iframe)  
        # print(i)
        i = i+1
        time.sleep(2)
        text = driver.page_source
        # print(text)
        # print('-'*50)
        text = text.lower()
        if "ad blocker" in text or "ad-blocker" in text:
            return 1
        driver.switch_to.default_content()
    return 0

def detect(driver):
    text = driver.page_source
    # print(text)
    text = text.lower()
    if "ad blocker" in text or "ad-blocker" in text:
        return 1
    return find_all_iframes(driver)

def initialize_driver(extn):
    # Prepare Chrome
    options = Options()
    # options.add_argument("--user-data-dir=/home/ritik/.config/google-chrome")
    # options.add_argument(f'--profile-directory={extn}')
    # Install other addons
    extensions_path = pathlib.Path("/home/ritik/work/pes/measurements/extensions/")

    matches = list(extensions_path.glob("{}*.crx".format(extn)))
    print(matches)
    if matches and len(matches) == 1:
        options.add_extension(str(matches[0]))
        # extn = extension

    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(30)
    time.sleep(10)
    return driver
        
def run(site_lst, extn, key, return_dict):
    # vdisplay = Display(visible=False, size=(1920, 1080))
    # vdisplay.start()
    driver = initialize_driver(extn)
    print(driver, site_lst)

    for site in site_lst:
        num_tries = 3 
        ret_val = 0

        while num_tries > 0:
            # print(site)
            # print(num_tries)
            driver.get(site)
            
            wait_until_loaded(driver, 30)
            time.sleep(3)

            ret_val = detect(driver)
            num_tries -= 1

            if ret_val:
                break

        if ret_val:
            f = open("blocking_urls.txt", "a+")
            f.write(driver.current_url)
            f.write('\n')
            f.close()

            return_dict[extn].append(key)
            break

    driver.quit()
    # vdisplay.stop()
    # print(return_dict)
# def start_detection(site_lst, extn, key, return_dict):
# run(["http://insider.com"], 'adblock', 'adblock', {'adblock': []})

# url1 = "http://businessinsider.com"
# url2 = "http://geeksforgeeks.org/python-lists/"
# url3 = "https://www.forbes.com/sites/kellyphillipserb/2023/04/09/swipe-right-on-your-1040ez-inside-the-tax-heaven-3000--dating-sim/?sh=d02b7a84cf28"
# run("http://insider.com", 'adblock')
# sys.exit(0)

# extn_lst = ['ublock', 'adblock', 'privacy-badger']

# threads = []

# for extn in extn_lst:
#     threads.append(threading.Thread(target=run, args=(site, extn,)))

# for t in threads:
#     t.start()

# for t in threads:
#     t.join()
