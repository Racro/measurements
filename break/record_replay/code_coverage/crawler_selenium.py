from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Chrome options
options = Options()
options.add_experimental_option("detach", True)
options.binary_location = "/home/ritik/work/pes/chrome_113/chrome"
service = Service(executable_path='/usr/local/bin/chromedriver')

# Initialize WebDriver
driver = webdriver.Chrome(service=service, options=options)

try:
    # Start CDP session and enable necessary domains
    driver.execute_cdp_cmd("Profiler.enable", {})
    driver.execute_cdp_cmd("Debugger.enable", {})

    # Start collecting coverage data
    driver.execute_cdp_cmd("Profiler.startPreciseCoverage", {"callCount": True, "detailed": True})

    # Your Selenium interactions here
    driver.get("https://www.google.com")
    time.sleep(5)
    # Stop collecting coverage data
    # driver.execute_cdp_cmd("Profiler.stopPreciseCoverage", {})

    # Retrieve the coverage data
    coverage_data = driver.execute_cdp_cmd("Profiler.takePreciseCoverage", {})

    print(coverage_data)
    # Process the coverage data as needed
    # ...

finally:
    # Quit the driver
    driver.quit()
