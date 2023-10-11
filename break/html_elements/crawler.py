from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time 
import json
import sys
import argparse
from selenium.common.exceptions import NoSuchElementException
import ast
import os

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

import re

login_keywords = [
    "log in",
    "log-in",
    "login",
    "sign in",
    "sign-in",
    "signin"
    "join "
]

def check_for_presence(lst):
    for word in lst:
        check = word
        if check.lower() in login_keywords:
            return word
    return ""

# Function to check for password field
def check_for_password_field(driver):
    # Look for password input fields
    password_fields = driver.find_elements(By.XPATH, '//input[@type="password"]')

    # Return True if any password fields were found, False otherwise
    return len(password_fields)

# def check_for_google(driver)


# url = "https://www.delta.com"
# try:
#     with open("../inner_pages_custom.json", "r") as f:
#         updated_dict = json.load(f)
#     f.close()
# except Exception as e:
#     print(e)
#     sys.exit(0)


# Initialize the driver (this will open a browser window)
# driver = webdriver.Chrome(executable_path='/path/to/chromedriver')


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
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-web-security")
options.add_argument("--disable-features=IsolateOrigins,site-per-process")
options.add_argument("--disable-features=AudioServiceOutOfProcess")
# options.add_argument("auto-open-devtools-for-tabs")
options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36") 
#options.add_extension("/home/seluser/measure/harexporttrigger-0.6.3.crx")
options.binary_location = "/home/ritik/work/pes/chrome_113/chrome"

def run(extn, sites):
    # Start X
    vdisplay = Display(visible=False, size=(1920, 1080))
    vdisplay.start()
    # options_extn = options
    if extn != "":
        options.add_extension(f'./../../extensions/extn_crx/{extn}.crx')
    # if extn != "":
    lst = []
    driver = webdriver.Chrome(options=options)
    time.sleep(1)

    for site in sites:       
        # Visit the website
        driver.get(site)
        wait_until_loaded(driver)
        time.sleep(10)
        driver.save_screenshot('before.png')

        js = '''return document.documentElement.outerHTML;'''

        # before DOM
        initial_passwd = check_for_password_field(driver)
        initial_dom = driver.execute_script(js)
        initial_url = driver.current_url
        initial_windows = len(driver.window_handles)

        after_dom = ""
        after_url = ""

        try:
            anchor_tag_text = driver.find_elements(By.TAG_NAME, 'a')
            button_text = driver.find_elements(By.TAG_NAME, 'button')

            a_tag_lst = []
            button_tag_lst = []

            for element in anchor_tag_text:
                a_tag_lst.append(element.text)

            for element in button_text:
                button_tag_lst.append(element.text)

            print(a_tag_lst)

            word = check_for_presence(a_tag_lst)
            if word:
                button_by_exact_text = driver.find_element(By.PARTIAL_LINK_TEXT, word)
            else:
                word = check_for_presence(button_tag_lst)
                
                if word:
                    button_by_exact_text = driver.find_element(By.XPATH, f"//button[contains(., '{word}')]")
                else:
                    continue

            if button_by_exact_text:
                button_by_exact_text.click()
                time.sleep(5)
                driver.save_screenshot('after.png')

                # This is the rendered DOM after JS execution
                after_dom = driver.execute_script(js)
                after_passwd = check_for_password_field(driver)
                after_url = driver.current_url
                after_windows = len(driver.window_handles)
                
                # print(driver.find_element(By.ID, 'loginPassword'))
                # sys.exit(1)
        except Exception as e:
            print(f'{site} ---- <button> ---- {e}', file=sys.stderr)
            continue

        # print('initial', initial_passwd, initial_windows)
        # print('after', after_passwd, after_windows)


        if after_url == "":
            print(f"No login button ---- {site} {extn}", file=sys.stderr)
            continue
        
        else:
            # compare the doms and urls
            if initial_url != after_url or after_windows > initial_windows or after_passwd > initial_passwd:
                continue
            initial_count = len(re.findall('password|continue\\ with\\ google|sign\\ in\\ with\\ google', initial_dom.lower())) #initial_dom.lower().count("password")
            after_count = len(re.findall('password|continue\\ with\\ google|sign\\ in\\ with\\ google', after_dom.lower())) #after_dom.lower().count("password")
            
            with open('after.out', 'w') as f:
                f.write(after_dom)
            f.close()
            with open('before.out', 'w') as f:
                f.write(initial_dom)
            f.close()
            
            if initial_count == after_count:
                # print(f'initial --- {initial_count}')
                # print(f'after --- {after_count}')
                lst.append(site.split("//")[1])

                # Define the directory and file name for the screenshot
                directory = f'./ss/{extn}'
                file_name = f'after_{site.split("//")[1]}.png'
                full_path = os.path.join(directory, file_name)

                # Check if the directory exists, create it if it doesn't
                if not os.path.exists(directory):
                    os.makedirs(directory)
                driver.save_screenshot(full_path)
    # Close the browser window
    driver.quit()
    vdisplay.stop()
    return lst

if __name__ == '__main__':
    # Parse the command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('website')
    parser.add_argument('--extension', type=str)
    # parser.add_argument('--extensions')
    # parser.add_argument('--extensions-wait', type=int, default=10)
    args = parser.parse_args()

    ret = run(args.extension, ast.literal_eval(args.website))
    # ret = run("", ast.literal_eval(args.website))
    # print(f'crawler ---- {ret}')
    print(ret)
