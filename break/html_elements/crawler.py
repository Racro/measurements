from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time 

url = "https://www.delta.com"

# Initialize the driver (this will open a browser window)
# driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
# Start X
# vdisplay = Display(visible=False, size=(1920, 1080))
# vdisplay.start()

# Prepare Chrome
options = Options()
#options.headless = False
# options.add_argument("--headless=new")
options.add_argument("no-sandbox")
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
options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36") 
#options.add_extension("/home/seluser/measure/harexporttrigger-0.6.3.crx")
options.binary_location = "/home/ritik/work/pes/chrome_113/chrome"

driver = webdriver.Chrome(options=options)

# Visit the website
driver.get(url)
driver.save_screenshot('delete.png')
time.sleep(5)
# click sign in button
# button_by_exact_text = driver.find_element(By.XPATH, "//button[contains(., 'REJECT')]")
# button_by_exact_text.click()
# time.sleep(2)

button_by_exact_text = driver.find_element(By.XPATH, "//button[contains(., 'Log')]")
button_by_exact_text.click()
time.sleep(2)

button_by_exact_text = driver.find_element(By.XPATH, "//button[contains(., 'Log')]")
button_by_exact_text.click()
time.sleep(2)

# This is the rendered DOM after JS execution
rendered_dom = driver.page_source

print(rendered_dom)

# Close the browser window
driver.quit()
