import os
import random
import time
import signal
import functools
import json
from time import sleep
from pyvirtualdisplay import Display
import inspect

# import pyautogui
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import NoSuchElementException, StaleElementReferenceException, InvalidSelectorException, ElementNotSelectableException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# Prepare Chrome
options = Options()
options.set_capability('goog:logginPrefs', {'browser': 'ALL'})
options.add_argument("start-maximized")
# options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_argument("--disable-animations")
options.add_argument("--disable-web-animations")
options.add_argument("--disable-gpu")

options.add_argument("--disable-features=IsolateOrigins,site-per-process")
options.add_argument("--disable-features=AudioServiceOutOfProcess")
options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36")
options.binary_location = "/home/mitch/work/pes/chrome_113/chrome"

log_file_path = "/home/mitch/measurements/break/html_elements/logs/chromedriver.log"
service = Service(executable_path='/home/mitch/work/pes/chromedriver_113/chromedriver', service_args=["--verbose", f"--log-path={log_file_path}"])
driver = webdriver.Chrome(options=options, service=service)

hierarchy_dict = {'buttons': [], "drop downs": [], "links": [], "login": []}
def generate_path(html_code):
    soup = BeautifulSoup(html_code, 'html.parser')
    tag = soup.find()
    tag_name = tag.name
    attributes = tag.attrs
    return tag_name, attributes

def generate_xpath(html_string):
    def parse_html_string(string):
        soup = BeautifulSoup(string, 'html.parser')
        if soup:
            tag = soup.find()
            if tag:
                tag_info = {
                    'tag_name': tag.name,
                    'attributes': tag.attrs
                }
                return tag_info
        return None

    def format_attribute(attr, value):
        if isinstance(value, list):
            return f'[contains(@{attr}, "{value[0]}")]'
        else:
            if "'" and '"' in value:
                return ''  # this case is too weird. will just skip it.
            elif "'" in value:
                return f"""[@{attr}="{value}"]"""
            return f"""[@{attr}='{value}']"""

    parsed_info = parse_html_string(html_string)
    if parsed_info:
        tag_name = parsed_info['tag_name']
        attributes = parsed_info['attributes']

        xpath = f'//{tag_name}'
        for attr, value in attributes.items():
            if attr == 'class':
                if isinstance(value, list):
                    for class_value in value:
                        xpath += f'[contains(@{attr}, "{class_value}")]'
                else:
                    xpath += f'[contains(@{attr}, "{value}")]'
            else:
                xpath += format_attribute(attr, value)

        return xpath
    return None

def get_local_DOM(self, elem):
    for i in range(self.DOM_traversal_amt):
        elem = elem.find_element(By.XPATH, '..')
    return elem.get_attribute('outerHTML')


def write_results():
    with open(f"hierarchy/final_results.json", 'w') as json_file:
        json.dump(hierarchy_dict, json_file)

def get_comparison_elms(element):
    outerHTML = element.get_attribute('outerHTML')
    DOM = driver.page_source
    URL = driver.current_url
    return outerHTML, DOM, URL


def hierarchy_change(html_obj, outerHTML, url):
    driver.get(url)
    time.sleep(5)
    xpath = generate_xpath(outerHTML)
    try:
        element = driver.find_element(By.XPATH, xpath)
    except Exception as e:
        print("can't find element. skip", url)
        write_results()
        return
    initial_outer, initial_DOM, initial_url = get_comparison_elms(element)

    try:
        driver.execute_script(
            "arguments[0].scrollIntoView({ behavior: 'auto', block: 'center', inline: 'center' });", element)
        time.sleep(1)
        element.click()
        time.sleep(1)
        try:
            element.click()
            time.sleep(1)
            element.click()
        except Exception as e:
            print("click button once!", url)

        if initial_url != driver.current_url:
            return
        time.sleep(3)
    except Exception as e:
        print("can't click on element", url)
        write_results()
        return


    all_windows = driver.window_handles

    # tests for more windows and will close them
    if len(all_windows) > 1:
        for window in all_windows[1:]:
            driver.switch_to.window(window)
            driver.close()
            driver.switch_to.window(all_windows[0])

    try:
        after_outer, after_DOM, after_url = get_comparison_elms(element)

        tag_initial, attribute_initial = generate_path(initial_outer)
        tag_after, attribute_after = generate_path(after_outer)

        control_code = BeautifulSoup(initial_DOM, 'html.parser')
        clicked_code = BeautifulSoup(after_DOM, 'html.parser')

        control = control_code.find(tag_initial, attribute_initial)
        clicked = clicked_code.find(tag_after, attribute_after)
    except Exception as e:
        print("element disappeared after click", url)
        write_results()
        return 0

    counter = None
    if control and clicked:
        counter = 0
        while control.parent and clicked.parent and control == clicked:
            control = control.parent
            clicked = clicked.parent
            counter += 1
        # if for some reason I cannot detect a change with the entire DOM something wierd probably happened
        if control == clicked:
            counter = None
        # hierarchy_dict[self.html_obj].append([site, outerHTML, control, clicked, counter])
        hierarchy_dict[html_obj].append([initial_url, outerHTML, counter])
    return counter


lst = ['buttons', 'login', 'drop downs', 'links']
for html_obj in lst:
    with open(f"json/{html_obj}_control.json", 'r') as file:
        json_data = json.load(file)
        sites = list(json_data.keys())
        for site in sites:
            for outerHTML in json_data[site]:
                hierarchy_change("buttons", outerHTML, site)

        with open(f"hierarchy/final_results.json", 'w') as json_file:
            json.dump(hierarchy_dict, json_file)
            exit(1)
        print("Done")

while 1:
    1

