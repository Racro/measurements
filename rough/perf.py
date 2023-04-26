from selenium import webdriver
from pyvirtualdisplay import Display
from selenium.webdriver.chrome.options import Options
import time

# Start the virtual display
display = Display(visible=0, size=(800, 600))
display.start()

# Create a webdriver instance with XVFB
options = Options()
options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')
options.add_argument("auto-open-devtools-for-tabs")
# options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

# Visit the website
driver.get('http://wikipedia.org')
time.sleep(2)
# Perform actions on the website (e.g. click buttons, fill forms, etc.)
# ...

navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
responseStart = driver.execute_script("return window.performance.timing.responseStart")
domComplete = driver.execute_script("return window.performance.timing.domComplete")
loadEnd = driver.execute_script("return window.performance.timing.loadEventEnd")

backendPerformance_calc = responseStart - navigationStart
frontendPerformance_calc = loadEnd - responseStart
print(navigationStart, responseStart, domComplete, loadEnd)
print(backendPerformance_calc, frontendPerformance_calc)

# Close the webdriver
driver.quit()

# Stop the virtual display
display.stop()