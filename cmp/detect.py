from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time 

options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)

driver.get('https://www.newbalance.com/')
time.sleep(2)
# Collect all the class names and ID names of the website's elements
class_names = []
id_names = []
elements = driver.find_elements(By.CSS_SELECTOR, '*')
for element in elements:
    try:
        if element.get_attribute('class'):
            class_names.extend(element.get_attribute('class').split())
        if element.get_attribute('id'):
            id_names.append(element.get_attribute('id'))
    except Exception as e:
        print(element)
# Search for a specific keyword in the collected class names and ID names
keyword = 'consent'
matching_class_names = [class_name for class_name in class_names if keyword in class_name]
matching_id_names = [id_name for id_name in id_names if keyword in id_name]

# Print the results
print('Matching class names:', matching_class_names)
print('Matching ID names:', matching_id_names)

# Close the web driver
driver.quit()