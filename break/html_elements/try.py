from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time 

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

driver = webdriver.Chrome(options=options)
driver.get("http://www.stackoverflow.com")
wait_until_loaded(driver)

header = driver.find_elements(By.TAG_NAME, "*")
print(str(len(header)))

import sys
# for i in header:
#     print(i.tag_name)
# header = header[7]
header = header[40]

print(header.is_enabled())
print()
print(header.text)
print()
print(header.tag_name)
print()
print(header.value_of_css_property('font-size'))
print()
print(header.get_attribute('href'))
print()
print(header.size)

# start from your target element, here for example, "header"
all_children_by_css = header.find_elements(By.CSS_SELECTOR, "*")
all_children_by_xpath = header.find_elements(By.XPATH, ".//*")

print('len(all_children_by_css): ' + str(len(all_children_by_css)))
print('len(all_children_by_xpath): ' + str(len(all_children_by_xpath)))

driver.quit()