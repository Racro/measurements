from xvfbwrapper import Xvfb
from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

import os
import sys
import time
import pickle as pk
from threading import Thread, Lock

from selenium.webdriver.chrome.options import Options

def iterate_and_add_text(extn, date_lst, text_lst, lock):
    if len(date_lst) != len(text_lst):
        print("list lengths not equal")
        exit(1)

    lock.acquire()
    for i in range(len(date_lst)):
        review_dict[extn][0].append(date_lst[i].text)
        review_dict[extn][1].append(text_lst[i].text)
    lock.release()

def write_to_pickle(data_str, filename):
    filehandler = open(filename, 'wb')
    pk.dump(data_str, filehandler)
    filehandler.close()

def write_to_textfile(data_str, filename):
    filehandler = open(filename, 'wt')
    filehandler.write(str(data_str))
    filehandler.close()

def pretty_write_to_textfile(data_str, filename):
    filehandler = open(filename, 'wt')
    for key in data_str:
        filehandler.write(key)
        filehandler.write('\n')
        filehandler.write(str(len(review_dict[key][0])))
        filehandler.write('\n')
        for j in range(len(review_dict[key][0])):
            filehandler.write(review_dict[key][0][j])
            filehandler.write("\n")
            filehandler.write(review_dict[key][1][j])
            filehandler.write("\n---------------------------------------\n")

        filehandler.write('\n'*3)
        filehandler.write("-----------------------------------------------------------------------"*2)
        filehandler.write('\n'*3)
    filehandler.close()

xf = Xvfb()  #  xf = Xvfb(1920, 1080) - will create virtual display with 1920x1080 size
xf.start()

categories = ['Arts and Entertainment', 'Business and Consumer Services', 'Community and Society', 'Computers Electronics and Technology', 'eCommerce and Shopping', 'Finance', 'Food and Drink', 'Gambling', 'Games', 'Health', 'Heavy Industry and Engineering', 'Hobbies and Leisure', 'Home and Garden', 'Jobs and Career', 'Law and Government', 'Lifestyle', 'News and Media Publishers', 'Pets and Animals', 'Reference Materials', 'Science and Education', 'Sports', 'Travel and Tourism', 'Vehicles', 'Adult']

category_dict = {} #the dict has the key as extn_id and value as pair of date_list and text_list
for category in categories:
    category_dict[category.replace(" ", "-")] = []

#for i in range(len(extn_lst)):
def get_category_list():#, lock):
    options = Options()
    
    # options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    url = "https://www.similarweb.com/"

    category_url = url + 'category/'
    print(category_url)

    category_class = 'tl-list__link'

    driver.get(category_url)
    time.sleep(5)

    category_elements = driver.find_elements(By.CLASS_NAME, value=category_class)

    url_lists = []
    root = url + "top-websites/"

    for element in category_elements:
        category = element.text.replace("&", "and")
        if len(category.split(' > ')) == 2:
            site1 = category.split(' > ')[0].replace(" ", "-")
            site2 = category.split(' > ')[1].replace(" ", "-")
            url_lists.append(root + site1 + "/" + site2)
        elif len(category.split(' > ')) == 1:
            site1 = category.split(' > ')[0].replace(" ", "-")
            url_lists.append(root + site1)
    
    driver.quit()
    return url_lists

def run_browser(site, category, l):
    options = Options()
    # options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    
    driver.get(site)
    time.sleep(5)
    
    sites_class = 'tw-table__row-compare'

    try:    
        website_elements = driver.find_elements(By.CLASS_NAME, value=sites_class)
    except Exception as e:
        print(e)
        print(f"no website elements for {site}")
        # print("continuing to next extension.....")
        # continue

    for w_element in website_elements:
        l.acquire()
        if w_element.text not in category_dict[category]:
            category_dict[category].append(w_element.text)
        l.release()
    # print(category_dict)
    driver.quit()

url_list = get_category_list()

threads = []
dict_lock = Lock()

for site in url_list:
    lst = site.split("/")
    if len(lst) == 6:
        category = lst[-2]
    elif len(lst) == 5:
        category = lst[-1]
    else:
        print(f"category not found for site: {site}")
        sys.exit(0)
    threads.append(Thread(target=run_browser, args=(site, category, dict_lock)))

def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]
    
SIZE = 10

chunks_list = list(divide_chunks(threads, SIZE))

for lst in chunks_list:
    for t in lst:
        print("starting threads")
        t.start()

    for t in lst:
        print("joining threads back in")
        t.join()

import json
f = open('website_categories.json', 'w')
json.dump(category_dict, f)
f.close()