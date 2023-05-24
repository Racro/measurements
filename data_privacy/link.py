from selenium import webdriver
from pyvirtualdisplay import Display
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from tranco import Tranco

t = Tranco(cache=True, cache_dir='.tranco')
latest_list = t.list()
sites = latest_list.top(500000)

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

def check_for_extn_installation(driver, name):  #generates a screenshot to check for extension installation
    # driver.get("https://chrome.google.com/webstore/detail/ghostery-%E2%80%93-privacy-ad-blo/mlomiejdfkolichcflejclcbmpeaniij?hl=en")
    #save screenshot
    S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
    driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment
    file_name = name + '.png'
    driver.find_element(by=By.TAG_NAME, value='body').screenshot(file_name)

# Start the virtual display
display = Display(visible=0, size=(800, 600))
display.start()

f = open('link.log', 'w')
# Create a webdriver instance with XVFB
options = Options()
count = 0
total = 0

# Visit the website
def crawl(sites, lock):
    global count
    global total
    driver = webdriver.Chrome(options=options)
    try:
        for site in sites:
            try:
                driver.get('http://'+site)
                # time.sleep(2)
                wait_until_loaded(driver)
                time.sleep(1)
            except Exception as e:
                continue
            
            lock.acquire()
            total += 1
            lock.release()
            text = driver.page_source
            idx = [0, 0, 0, 0]
            if 'rel="prefetch"' in text or 'rel=prefetch' in text or 'rel=dns-prefetch' in text or 'lazyload>' in text:
                idx[0] = text.find('rel="prefetch"')
                idx[1] = text.find('rel=prefetch')
                idx[2] = text.find('rel=dns-prefetch')
                idx[3] = text.find('lazyload>')
                
                to_print = ""
                for i in idx:
                    if i > 0 :
                        to_print = text[i-50:i+50]
                        break

                print(f'{site}: {to_print}')
                f.write(f'{site}: ')
                f.write(to_print)
                f.write('\n')
                lock.acquire()
                count += 1
                lock.release()

    except KeyboardInterrupt as k:
        print(count, total)
        driver.close()
        return
    except Exception as e:
        print(count, total)
        driver.close()
        return

    print(count, total)
    driver.close()

import multiprocessing
import threading

def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]

chunks_list = list(divide_chunks(sites, 5000))
threads = []
lock = threading.Lock()
print(chunks_list)

for i in chunks_list:
    p = threading.Thread(target=crawl, args=(i, lock,))
    threads.append(p)

try:
    for t in threads:
        t.start()

    for t in threads:
        t.join()
except KeyboardInterrupt as k:
    import sys
    print(f'Total count: {count}')
    print(f'Total crawls: {total}')
    sys.exit(1)

print(f'Total count: {count}')
print(f'Total crawls: {total}')



f.close()

# Stop the virtual display
display.stop()
