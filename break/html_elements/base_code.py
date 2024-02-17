import os
import random
import time
import signal
import functools
import json
from time import sleep
from pyvirtualdisplay import Display

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

from Excel import *
# from functions import *

options = Options()
# options.headless = False
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
options.add_argument(
    "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36")

options.binary_location = '/usr/local/bin/chrome_113/chrome'

# folder_path = f"/home/chatacter/wpr_data/"
# if not os.path.exists(folder_path):
# # Create the folder
#     os.makedirs(folder_path)
#
# # options.add_argument('--ignore-certificate-errors')
# options.add_argument(folder_path)
# options.add_argument(f'--host-resolver-rules="MAP *:80 127.0.0.1:9090,MAP *:443 127.0.0.1:9091,EXCLUDE localhost')
# options.add_argument('--ignore-certificate-errors-spki-list=PhrPvGIaAMmd29hj8BCZOq096yj7uMpRNHpn5PDxI6I=,2HcXCSKKJS0lEXLQEWhpHUfGuojiU0tiT5gOF9LP6IQ=')

"""
cd /go/src/catapult/web_page_replay_go

go run src/wpr.go record --http_port=9090 --https_port=9091 ~/control.wprgo
go run src/wpr.go replay --http_port=9090 --https_port=9091 ~/control.wprgo
"""

attributes_dict = {
    "buttons": {
        "attributes": ['button', 'submit', '#'],
        "xpaths": ['@role', '@type']
    },
    "drop downs": {
        "attributes": ['false', 'true', 'main menu', 'open menu', 'all microsoft menu', 'menu', 'navigation',
                       'primary navigation', 'hamburger', 'settings and quick links', 'dropdown', 'dialog',
                       'js-menu-toggle', 'searchDropdownDescription', 'ctabutton',
                       'legacy-homepage_legacyButton__oUMB9 legacy-homepage_hamburgerButton__VsG7q',
                       'Toggle language selector', 'Open Navigation Drawer', 'guide', 'Expand Your Library',
                       'Collapse Your Library'],
        "xpaths": ['@aria-expanded', '@aria-label', '@class', '@aria-haspopup', '@aria-describedby', '@data-testid']
    },
    "links": {
        "attributes": [],
        "xpaths": ['href']
    },
    "login": {  # remember to enable HREF
        "attributes": ['button', 'submit', '#'],
        "xpaths": ['@role', '@type']
    }
    , "manual": {
        "attributes": [],
        "xpaths": []
    }

}

def error_catcher(e, driver, tries, url):
    error = ''
    if driver.tries != 3:
        driver.reinitialize()
        tries += 1
        return tries

    # if isinstance(e, ElementClickInterceptedException):
    #     error = "N/A - Element Click Intercepted"
    if isinstance(e, ElementNotSelectableException):
        error = "N/A - Not Selectable"
    elif isinstance(e, StaleElementReferenceException):
        error = "StaleElementReferenceException"
    elif isinstance(e, NoSuchElementException):
        error = "N/A - No such Element"
    elif isinstance(e, InvalidSelectorException):
        error = "N/A - InvalidSelectorException"
    elif isinstance(e, IndexError):
        error = e
    elif isinstance(e, TimeoutError):
        print("Timeout")
        # write_noscan_row(url)
        tries = 1
        driver.tries = 1
        driver.curr_elem += 1
        print("TIME OUT EERRORRR")
        return tries
    else:
        error = str(e).split("\n")[0]
    return error


class TimeoutError(Exception):
    pass


def timeout(seconds):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            def handler(signum, frame):
                raise TimeoutError

            signal.signal(signal.SIGALRM, handler)
            signal.alarm(seconds)

            result = func(*args, **kwargs)
            signal.alarm(0)
            return result

        return wrapper

    return decorator


class Driver:
    def __init__(self, attributes, xPATH, adB, html_obj, replay, data_dict, excel_dict):
        # specific test for these attributes
        self.attributes = attributes
        self.xPaths = xPATH

        # initializing the adBlocker
        self.adBlocker_name = adB
        self.driver = None
        self.tries = 1
        self.vdisplay = ''

        # used for optimization
        self.keywords = [
            'login', 'my account', 'sign in', 'sign-in', 'signin', 'log in',  # English
            '登录', '我的帐户',  # Chinese (Simplified)
            'вход', 'войти', 'мой аккаунт',  # Russian
            'iniciar sesión', 'mi cuenta'  # Spanish
        ]
        self.seen_sites = []
        self.xpath_remover = 3
        self.website_sleep_time = 3  # longer this value, more consistent the results
        self.html_obj = html_obj
        self.DOM_traversal_amt = 4
        self.scan_timeout = 180
        self.test_elem_timeout = 300

        # used for testing
        self.curr_site = 0
        self.curr_elem = 0
        self.initial_outer_html = ''
        self.after_outer_html = ''
        self.initial_local_DOM = ''
        self.after_local_DOM = ''
        self.url = ''
        self.url_key = ''
        self.redirect_url = ''
        self.DOM_changed = False
        self.outer_HTML_changed = False

        # used for random picking
        self.dictionary = data_dict
        self.excel = excel_dict
        self.excel_list = []
        self.excel_errors_list = []

        self.all_sites = {}
        self.no_elms = 15
        self.chosen_elms = []
        self.all_html_elms = []

        #### RITIK
        self.options = ''
        self.replay = replay

    def initialize(self, options, num_tries, url):
        """
            This function will start a Chrome instance with the option of installing an ad blocker.
            Adjust the seconds parameter so that it will wait for the ad blocker to finish downloading.
        """
        self.url_key = url

        while num_tries > 0:
            try:
                self.options = options
                self.driver = webdriver.Chrome(options=options)
                self.driver.set_page_load_timeout(45)
                time.sleep(2)
                break
            except Exception as e:
                if num_tries == 0:
                    print(1, e)
                    return 0
                else:
                    print("couldn't create browser session... trying again")
                    num_tries = num_tries - 1

        # during replay phase
        if self.replay:
            file_path = f"data_1000/json/{self.html_obj}_control.json"
            # self.excel[self.adBlocker_name][self.html_obj][self.url_key] = []
            # self.excel['errors'][self.adBlocker_name][self.html_obj][self.url_key] = []

            try:
                if os.path.isfile(file_path):
                    with open(file_path, 'r') as json_file:
                        self.dictionary = {}
                        self.dictionary[self.adBlocker_name] = {}
                        self.dictionary[self.adBlocker_name][self.html_obj] = {}
                        self.dictionary[self.adBlocker_name][self.html_obj][self.url_key] = json.load(json_file)[self.url_key] 
                        # self.dictionary[self.url_key] = json.load(json_file)[self.url_key]
                    json_file.close()
                elems = self.dictionary[self.adBlocker_name][self.html_obj][self.url_key]
                self.all_sites = [self.url_key]
            except KeyError as k:
                print(f"site not found in json --- site:{self.url_key}, extn:{self.adBlocker_name}, html: {self.html_obj}")
                return 0
            except Exception as e:
                print(4, e)
                return 0
        
        time.sleep(2)

        if self.adBlocker_name == 'adblock':
            time.sleep(15)
        elif self.adBlocker_name == 'ghostery':
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
        return 1

    def is_loaded(self):
        return self.driver.execute_script("return document.readyState") == "complete"

    def wait_until_loaded(self, timeout=60, period=0.25, min_time=0):
        start_time = time.time()
        mustend = time.time() + timeout
        while time.time() < mustend:
            if self.is_loaded():
                if time.time() - start_time < min_time:
                    time.sleep(min_time + start_time - time.time())
                return True
            time.sleep(period)
        return False

    def load_site(self, url):
        """
            makes selenium load the site. will add http://www. if needed and filters out to see if the website is
            accessible or not.
        """
        try:
            self.driver.get(url)
            self.wait_until_loaded()
            time.sleep(2)

            self.url = self.driver.current_url
            # self.url_key = url
            if self.url not in self.seen_sites:
                # write_results(self.url)
                self.seen_sites.append(self.url)
            return True

        except Exception as e:
            self.dictionary['errors'][self.adBlocker_name][self.url_key] = str(e)
            print(3, e)
            self.seen_sites.append(url)
            return False
        
    # def remove_stuff(self):
    #     remove_popup(self.driver)
    #     remove_alert(self.driver) # optional

    def reinitialize(self):
        self.driver.close()
        self.initialize(self.options, 3, self.url_key)
        self.tries += 1

    def scroll(self):
        curr_scroll_position = -1
        curr_time = time.time()
        while True:
            # Define the scroll step size
            scroll_step = 50  # Adjust this value to control the scroll speed
            # Get the current scroll position
            scroll_position = self.driver.execute_script("return window.pageYOffset;")
            # Check if we've reached the bottom
            if curr_scroll_position == scroll_position:
                break
            else:
                curr_scroll_position = scroll_position

            # Scroll down by the step size
            self.driver.execute_script(f"window.scrollBy(0, {scroll_step});")
            
            # Wait for a bit (this controls the scroll speed indirectly)
            time.sleep(0.1)  # Adjust this value to control the scroll speed
            if time.time() - curr_time >= 45:
                break

    def close(self):
        print("closing driver...", self.adBlocker_name, self.html_obj, self.url)
        if self.driver != None:
            self.driver.quit()
        # self.vdisplay.stop()

    def click_button(self, button):
        try:
            button.click()
        except Exception:
            self.driver.execute_script(
                "arguments[0].scrollIntoView({ behavior: 'auto', block: 'center', inline: 'center' });", button)
            sleep(2)
            button.click()

    def cursor_change(self, element):
        actions = ActionChains(self.driver)
        # print(element.get_attribute('outerHTML'))
        try:
            actions.move_to_element(element).perform()
            sleep(1)
            cursor_property = element.value_of_css_property('cursor')
            if cursor_property == 'pointer':
                return True
            else:
                return False
        except Exception as e:
            return False

    def check_redirect(self, url):
        def are_urls_equal(url1, url2):
            path1 = url1.rstrip('/').strip('https://').strip('www.')
            path2 = url2.rstrip('/').strip('https://').strip('www.')
            return path1 == path2

        sleep(3)
        if not are_urls_equal(self.driver.current_url, url):
            return True, self.driver.current_url

        all_windows = self.driver.window_handles

        # tests for more windows and will close them
        if len(all_windows) > 1:
            for window in all_windows[1:]:
                self.driver.switch_to.window(window)
                self.driver.close()
            self.driver.switch_to.window(all_windows[0])
            return True, self.driver.current_url
        return False, self.driver.current_url

    def count_tags(self):
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        tags = soup.find_all()
        return len(tags)

    def get_local_DOM(self, elem):
        for i in range(self.DOM_traversal_amt):
            elem = elem.find_element(By.XPATH, '..')
        return elem.get_attribute('outerHTML')

    def generate_xpath(self, html_string):
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
            # if "'" in value:
            #     value_lst = value.split("'")
            #     return "[contains(@" + attr + ", " + "concat(" + value_lst[0] + ", \"'\", " + value_lst[1] + ", \"'\", " + value_lst[2] + "))]"

            if isinstance(value, list):
                return f'[contains(@{attr}, "{value[0]}")]'
            else:
                if "'" and '"' in value:
                    return ''           # this case is too weird. will just skip it.
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

    def get_correct_elem(self, xpath):
        counter = self.xpath_remover
        while "[" in xpath and counter:
            elements = self.driver.find_elements(By.XPATH, xpath)  # will return [] if none are found
            for i in elements:
                if i.get_attribute("outerHTML") == self.initial_outer_html:
                    return i
            try:    # sometimes the structure is the same.
                return self.driver.find_element(By.XPATH, xpath)
            except Exception:
                xpath_list = xpath.split("[")
                xpath_list.remove(max(xpath_list, key=len))
                xpath = "[".join(xpath_list)
            self.xpath_remover -= 1
        self.xpath_remover = 3
        return self.driver.find_element(By.XPATH, xpath)  # will error if none are found

    def check_opened(self, url, button, initial_tag):
        def check_HTML(initial, after):
            if initial != after:
                return True
            return False

        redirect, new_url = self.check_redirect(url)
        if redirect:
            return "True - Redirect"

        try:
            self.after_outer_html = button.get_attribute('outerHTML')
        except StaleElementReferenceException:
            # this is good, means that the button disappeared after clicking
            # could be things like "close", "search", "expand", "show more", etc.
            return "True - Stale Element"

        self.DOM_changed = check_HTML(self.initial_local_DOM, self.get_local_DOM(button))
        self.outer_HTML_changed = check_HTML(self.initial_outer_html, self.after_outer_html)

        if self.outer_HTML_changed:
            return "True - outerHTML change"

        if self.DOM_changed:
            return "True? - Local DOM Change"

        if self.count_tags() > initial_tag:
            return "True - More Tags"

        return "False"

    @timeout(300)
    def test_button(self, tries):
        site = self.all_sites[self.curr_site]
        try:
            outerHTML = self.dictionary[self.adBlocker_name][self.html_obj][site][self.curr_elem]
            xpath = self.generate_xpath(outerHTML)
        except IndexError as e:
            self.excel_errors_list.append(['IndexError: list is empty', '', '', self.initial_outer_html, '', '', '',
                           self.url_key, self.driver.current_url, tries])
            return

        except Exception as e:
            print(e)
            self.excel_errors_list.append(["Unknown Exception", '', '', self.initial_outer_html, '', '', '',
                           self.url_key, self.driver.current_url, tries])
            return

        self.load_site(site)
        self.initial_outer_html = outerHTML
        element = self.get_correct_elem(xpath)
        self.initial_local_DOM = self.get_local_DOM(element)

        initial_tag = self.count_tags()

        self.click_button(element)

        check = self.check_opened(self.url, element, initial_tag)

        if check == "True - Redirect":
            # outer_HTML_change = url
            # Dom_change = new_url
            self.excel_list.append([check, '', '', self.initial_outer_html, '', '', '',
                           self.url, self.driver.current_url, tries])
        elif check == "True - outerHTML change" or check == "True - Stale Element":
            self.excel_list.append([check, self.outer_HTML_changed, self.DOM_changed, self.initial_outer_html,
                           self.after_outer_html, '', '', '', '', tries])

        elif check == "True? - Local DOM Change":
            # need to figure out algo after find the difference
            self.excel_list.append([check, self.outer_HTML_changed, self.DOM_changed, self.initial_outer_html, '',
                           self.initial_local_DOM, self.after_local_DOM, '', '', tries])

        elif check == "False":
            self.excel_list.append([check, "False", "False", self.initial_outer_html, '',
                           "", "", '', '', tries])

    def click_on_elms(self, tries):
        while self.curr_site < len(self.all_sites):
            # print(f'curr_site: {self.curr_site}, all_sites: {self.all_sites}, curr_elem: {self.curr_elem}, xpaths: {self.dictionary[self.adBlocker_name][self.html_obj][self.all_sites[self.curr_site]]}')
            if self.curr_elem >= len(self.dictionary[self.adBlocker_name][self.html_obj][self.all_sites[self.curr_site]]):
                self.curr_site += 1
                self.curr_elem = 0
            else:
                self.test_button(tries)
                self.curr_elem += 1
            
        self.curr_site = -1
        self.excel[self.adBlocker_name][self.html_obj][self.url_key] = self.excel_list
        self.excel['errors'][self.adBlocker_name][self.html_obj][self.url_key] = self.excel_errors_list

    ############################################################

    """            
            FINDING AND FILTERING THE HTML Elements
    """

    ############################################################
    @timeout(300)
    def scan_page(self):
        self.load_site(self.url)  # extra refresh helps get rid of some false findings
        self.get_elements()
        self.dictionary[self.adBlocker_name][self.html_obj][self.url_key] = self.chosen_elms
        # print(self.chosen_elms)

        while self.curr_elem < len(self.dictionary[self.adBlocker_name][self.html_obj][self.url_key]):
            try:
                xpath = self.generate_xpath(self.dictionary[self.adBlocker_name][self.html_obj][self.url_key][self.curr_elem])
                elm = self.get_correct_elem(xpath)
                elm.click()
                sleep(1)
                self.load_site(self.url)
            except Exception as e:
                # print(e)
                # print("error in clicking element or generating xpath")
                pass
            all_windows = self.driver.window_handles

            # tests for more windows and will close them
            if len(all_windows) > 1:
                for window in all_windows[1:]:
                    self.driver.switch_to.window(window)
                    self.driver.close()
                self.driver.switch_to.window(all_windows[0])
                
            self.curr_elem += 1
        self.curr_elem = 0
        self.curr_site += 1

        # storeDictionary(self.dictionary[self.adBlocker_name][self.html_obj], self.html_obj, self.adBlocker_name)

    def make_unique(self, potential):
        self.chosen_elms = [elem.get_attribute("outerHTML") for elem in potential]
        self.chosen_elms = list(set(self.chosen_elms))

    def get_elements(self):
        # returns the contents (will be selenium objs)
        ret = []
        if self.html_obj == "drop downs":
            ret = self.find_dropdown()
        elif self.html_obj == "buttons":
            ret = self.find_buttons()
        elif self.html_obj == "links":
            ret = self.find_links()
        elif self.html_obj == "login":
            ret = self.find_login()
        else:
            print("Invalid Element type to retrieve")

        if self.html_obj == "login":
            final_lst = []
            for i in range(len(ret)):
                try:
                    if self.filter(ret[i]):
                        final_lst.append(ret[i])
                except Exception as e:
                    continue
        else:
            random.shuffle(ret)
            final_lst = []
            limit = min(15, len(ret))
            i = 0
            while len(final_lst) < limit and i < len(ret):
                if self.filter(ret[i]):
                    final_lst.append(ret[i])
                i += 1

        self.make_unique(final_lst)         # unique by looking at the outerHTML

        # the chosen_elms will be the unique outerHTML
        # if len(self.chosen_elms) <= self.no_elms:
        #     write_results(f"testing {len(self.chosen_elms)} / {len(self.chosen_elms)}")
        # else:
        #     write_results(f"testing {len(self.chosen_elms)} / {self.no_elms}")

    def filter(self, element):

        if self.html_obj == "login":
            if any(keyword.lower() in element.text.lower() for keyword in self.keywords):
                if self.cursor_change(element):
                    print(f"{self.url} \t {element.text}")
                    return True
        elif self.cursor_change(element):  # and element.is_displayed()   not always working correctly :(
            return True
        else:
            return False

    def specific_element_finder(self, found_elements=None):
        # will just add on to the current found_elements list.
        if not found_elements:
            found_elements = []
        for attribute in self.attributes:
            for path in self.xPaths:
                xpath = (f'//*[translate({path}, "ABCDEFGHIJKLMNOPQRSTUVWXYZ", '
                         f'"abcdefghijklmnopqrstuvwxyz")="{attribute.lower()}"]')
                try:
                    elements = self.driver.find_elements(By.XPATH, xpath)
                    for element in elements:
                        if element not in found_elements:
                            if self.html_obj == "buttons" and "href" not in element.get_attribute("outerHTML"):
                                found_elements.append(element)
                            else:
                                found_elements.append(element)
                except Exception as e:
                    self.dictionary['errors'][self.adBlocker_name][self.url_key] = str(e)
                    print(2, e)
        return found_elements

    def find_buttons(self):
        def collect():
            found_elements = self.driver.find_elements(By.TAG_NAME, 'button')
            for anchor in self.driver.find_elements(By.TAG_NAME, 'a'):
                if anchor.get_attribute("href") is None:
                    found_elements.append(anchor)

            final = self.specific_element_finder(found_elements)
            return final

        try:
            ret = collect()
            return ret
        except Exception as e:  # not tested
            try:
                sleep(5)
                return collect()
            except Exception as e:
                error_message = [str(e).split('\n')[0], "Failed to scrape Site", "", "", ""]
                self.excel_errors_list.append(error_message)

    def find_dropdown(self):
        try:
            ret = self.specific_element_finder()
            return ret
        except Exception as e:
            try:
                sleep(5)
                return self.specific_element_finder()
            except Exception as e:
                error_message = [str(e).split('\n')[0], "Failed to scrape Site", "", "", ""]
                self.excel_errors_list.append(error_message)

    def find_links(self):
        def collect():
            final = []
            for anchor in self.driver.find_elements(By.TAG_NAME, 'a'):
                if anchor.get_attribute("href"):
                    final.append(anchor)

            return final

        try:
            ret = collect()
            return ret
        except Exception as e:  # not tested
            try:
                sleep(5)
                return collect()
            except Exception as e:
                error_message = [str(e).split('\n')[0], "Failed to scrape Site", "", "", ""]
                self.excel_errors_list.append(error_message)

    def find_login(self):
        def collect():
            found_elements = self.driver.find_elements(By.TAG_NAME, 'button')
            found_elements += self.driver.find_elements(By.TAG_NAME, 'a')
            final = self.specific_element_finder(found_elements)
            return final

        try:
            ret = collect()
            # for i in ret:
            #     print(i.get_attribute("outerHTML"))
            return ret
        except Exception as e:  # not tested
            try:
                sleep(5)
                return collect()
            except Exception as e:
                error_message = [str(e).split('\n')[0], "Failed to scrape Site", "", "", ""]
                self.excel_errors_list.append(error_message)


# self.driver = Driver()
