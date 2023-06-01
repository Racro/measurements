# from xvfbwrapper import Xvfb
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui

import os
import sys
import time
import argparse
import pathlib
#from bs4 import BeautifulSoup as bs 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# def check_for_extn_installation(driver, name):  #generates a screenshot to check for extension installation
#     driver.get("https://chrome.google.com/webstore/detail/ghostery-%E2%80%93-privacy-ad-blo/mlomiejdfkolichcflejclcbmpeaniij?hl=en")
#     #save screenshot
#     S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
#     driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment
#     file_name = name + '.png'
#     driver.find_element(by=By.TAG_NAME, value='body').screenshot(file_name)

def extension_add(opts, extn): #adds extension
    opts.add_extension(extn)
    return opts

# def dwn_path_add(opts, pth): #adds download path to download fingerprints
#     prefs = {"download.default_directory" : pth}
#     opts.add_experimental_option("prefs",prefs)

# xf = Xvfb()  #  xf = Xvfb(1920, 1080) - will create virtual display with 1920x1080 size
# xf.start()
# browser won't appear
vdisplay = Display(visible=False, size=(1920, 1080))
vdisplay.start()

# extn_lst = ['', 'grammarly', 'gtranslate', 'honey', 'windows', 'cisco', 'tamper', 'netflix', 'scrcast', 'metamask']
#extn_lst = ['adobe', 'grammarly', 'honey', 'gtranslate', 'windows', 'tamper', 'netflix', 'scrcast', 'cisco', 'metamask']

# extn_lst = ['scriptsafe']
# extn_lst = [ 'control', 'adblock', 'ublock', 'privacy-badger',
#        "decentraleyes",
#        "disconnect",
#        "ghostery",
#        "https",
#        "noscript",
#        "scriptsafe",
#        "canvas-antifp",
#        "adguard"]

parser = argparse.ArgumentParser()
parser.add_argument('--extensions')
args = parser.parse_args()

i = args.extensions

options = Options()
#options.headless = False
# options.add_argument("--headless=new")
options.add_argument("no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("auto-open-devtools-for-tabs")
options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36") 
#options.add_extension("/home/seluser/measure/harexporttrigger-0.6.3.crx")
options.binary_location = "/usr/bin/google-chrome"

# cwd = os.getcwd() #assuming that the script is run inside the repo
extensions_path = pathlib.Path("/home/seluser/measure/extensions/extn_crx")
pth = list(extensions_path.glob("{}*.crx".format(i)))
if i != 'control':
    options = extension_add(options, str(pth[0]))
#pth = '/home/ritik/pes/ghostery.zip'
print(i)
print("###########################")



driver = webdriver.Chrome(options=options)
time.sleep(10)
#check_for_extn_installation(driver, i)

driver.get("https://coveryourtracks.eff.org/")
time.sleep(5)

# initial_html = driver.page_source

element = driver.find_element(By.ID, "kcarterlink")
element.click()

# wait.until(lambda driver: driver.find_element(By.ID, "results"))
try:
    element = WebDriverWait(driver, 360).until(
        EC.presence_of_element_located((By.CLASS_NAME, "entropy"))
    )
except Exception as e:
    print(e)
    sys.exit(1)

####
# entropy = driver.find_element(By.CLASS_NAME, value="entropy")
# print(i)
bits = element.text
index = bits.index("bits")
print(bits[index-7:index+4])
####
# driver.quit()
# continue
#####
result = driver.find_element(By.ID, value="fp_status")
print(result.text)
if i == "control":
    file_name = "/data/none.fp"
else:
    file_name = "/data/"+i+".fp"
f = open(file_name, "w")
f.write(bits[index-7:index+4])
f.write('\n')
f.write(result.text)

# for i in result:
    #html = i.get_attribute('innerHTML')
    # info = i.text.split('\n')
    # f.write(info[0])
    # f.write('\n')
    # f.write(info[1])
    # f.write('\n')
    # f.write(info[2])
    # f.write('\n')
f.close()
#####

#    fp = driver.find_element(By.ID, "fp_status")
#    tracker = driver2.find_element(By.ID, "tracker_status")
#    ad = driver3.find_element(By.ID, "ad_status")
#    
#    try:
#        fp_entropy = driver4.find_element(by=By.CLASS_NAME, value="entropy")
#        print("entropy?", fp_entropy.text)
#    except:
#        print("XXXXXXXXXX")
#        print("entropy not present")
#    print("fingerprint? ", fp.text)
#    #print("fingerprint_text?", fp.get_attribute('innerHTML'))
#    print("tracking_blocked? ", tracker.text)
#    print("ad_blocked? ", ad.text

driver.quit()
# xf.stop()