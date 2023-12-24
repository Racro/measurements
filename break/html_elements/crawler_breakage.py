from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException

import time 
import multiprocessing
import json
import argparse
import os
import subprocess
from pyvirtualdisplay import Display
import sys
import random
import math
from functions import *
import signal
        
extn_lst = [
     'control'
    #  , 'adblock', 'ublock', 'privacy-badger',
    #     "ghostery",
    #     "adguard"
    ]

def run(site, extn, return_dict, l, replay, temp_port1):
    # Prepare Chrome
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-animations")
    options.add_argument("--disable-web-animations")
    options.add_argument("--disable-gpu")

    options.add_argument("--disable-features=IsolateOrigins,site-per-process")
    options.add_argument("--disable-features=AudioServiceOutOfProcess")
    options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36")
    options.binary_location = "/home/ritik/work/pes/chrome_113/chrome"
    
    options = remove_cmp_banner(options)
    options = use_catapult(options, extn, temp_port1)

    if extn != 'control':
        options.add_extension(f'/home/ritik/pes/measurements/extensions/extn_crx/{extn}.crx')

    vdisplay = Display(visible=False, size=(1920, 1280))
    vdisplay.start()

    driver = webdriver.Chrome(options=options)
    time.sleep(2) # wait for extension to load

    if extn == 'adblock':
        time.sleep(15)
    elif extn == 'ghostery':
        windows = driver.window_handles
        for window in windows:
            try:
                driver.switch_to.window(window)
                url_start = driver.current_url[:16]
                if url_start == 'chrome-extension':
                    element = driver.find_element(By.XPATH, "//ui-button[@type='success']")
                    element.click()
                    time.sleep(2)
                    break
            except Exception as e:
                print('ghostery', 1, e)
                return

    driver.get(site)
    wait_until_loaded(driver)
    time.sleep(2)

    remove_popup(driver)
    remove_alert(driver) # optional

    if replay == 0: # can add clicking on the buttons
        # scroll
        curr_scroll_position = -1
        curr_time = time.time()
        while True:
            # Define the scroll step size
            scroll_step = 50  # Adjust this value to control the scroll speed
            # Get the current scroll position
            scroll_position = driver.execute_script("return window.pageYOffset;")
            # Check if we've reached the bottom
            if curr_scroll_position == scroll_position:
                break
            else:
                curr_scroll_position = scroll_position

            # Scroll down by the step size
            driver.execute_script(f"window.scrollBy(0, {scroll_step});")
            
            # Wait for a bit (this controls the scroll speed indirectly)
            time.sleep(0.1)  # Adjust this value to control the scroll speed
            if time.time() - curr_time >= 45:
                break

        # click

    if replay:
        # click and compare




        breakages = [] # list of breakages found

        # function to test breakages
        
        try:
            l.acquire()
            # print(fname)
            return_dict[extn][site].extend([breakages])
            l.release()
        except Exception as e:
            print(e)
            l.release()

    driver.quit()
    vdisplay.stop()

SIZE = 20
port = 9090

if __name__ == "__main__":
    # Parse the command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--replay', type=int)
    if len(sys.argv) < 2:
        parser.print_help(sys.stderr)
        sys.exit(1)
    args = parser.parse_args()

    ports_list = []

    # processes = []

    try:
        with open("../../break/adblock_detect/inner_pages_custom_break.json", "r") as f:
            updated_dict = json.load(f)
        f.close()

        # filtering the landing pages
        websites = []
        for key in updated_dict:
            websites.append(updated_dict[key][0])
        
        websites = random.sample(websites, 200)
        
        num_servers = math.ceil(len(websites)/100)
        print(num_servers)

        website_dict = {}
        for i in range(num_servers):
            if i == num_servers - 1:
                website_dict[i] = websites[100*i:]
            else: 
                website_dict[i] = websites[100*i:100*(i+1)]

        with open('manual_analysis.json', 'w') as f:
            json.dump(website_dict, f)
        f.close()

        # chunks_list = list(divide_chunks(websites, SIZE))
        chunks_list = list(website_dict.values())
        
        # multiprocess
        manager = multiprocessing.Manager()
        return_dict = manager.dict()
        result_dict = {}
        for extn in extn_lst:
            folder_path = f'/home/ritik/pes/measurements/break/html_elements/wpr_data/{extn}'
            if not os.path.exists(folder_path):
            # Create the folder
                os.makedirs(folder_path)

            return_dict[extn] = manager.dict()
            result_dict[extn] = {}
            
            num_chunks = len(chunks_list)
            for i in range(num_chunks):
                chunks_list[i] = list(divide_chunks(chunks_list[i], 10))
            
            print(chunks_list)
            i = 0
            while i < num_chunks:
                processes = start_servers(args.replay, i, extn)
                ports_list.append(port + 2*i)
                ports_list.append(port + 2*(i+1))

                for j in range(len(chunks_list[i])):
                    print('-'*50)
                    print('j:', j)
                    jobs = []
                    for k in range(len(chunks_list[i][j])):
                        return_dict[extn][chunks_list[i][j][k]] = manager.list()
                        result_dict[extn][chunks_list[i][j][k]] = []
                        p1 = multiprocessing.Process(target=run, args=(chunks_list[i][j][k], extn, return_dict, multiprocessing.Lock(), args.replay, port + 2*i, ))
                        jobs.append(p1)
                        
                        if i+1 != num_chunks:
                            return_dict[extn][chunks_list[i+1][j][k]] = manager.list()
                            result_dict[extn][chunks_list[i+1][j][k]] = []
                            p2 = multiprocessing.Process(target=run, args=(chunks_list[i+1][j][k], extn, return_dict, multiprocessing.Lock(), args.replay, port + 2*(i+1), ))
                            jobs.append(p2)
                    
                    for job in jobs:
                        job.start()
                    for job in jobs:
                        job.join()
                
                i = i+2
                time.sleep(2)
                
                print(f"Closing opened servers with ports: {port+2*(i-2)} {port+2*(i-1)}")

                try:
                    pid1 = get_pid_by_port(port+2*(i-2))
                    pid2 = get_pid_by_port(port+2*(i-1))
                    print(pid1, pid2)
                    
                    if pid1 != None:
                        os.kill(int(pid1), signal.SIGINT)
                        time.sleep(2)
                    ports_list.remove(port+2*(i-2))

                    if pid2 != None:
                        os.kill(int(pid2), signal.SIGINT)
                        time.sleep(2)
                    ports_list.remove(port+2*(i-1))

                except ProcessLookupError:
                    print(f"No process with PID {pid1} found.")
                except PermissionError:
                    print(f"Permission denied to send signal to process {pid1}.")
                
            if args.replay:                
                for site in websites:
                    print(return_dict[extn][site])
                    for val in return_dict[extn][site]:
                        result_dict[extn][site].append(val)

                f = open('html_breakages.json', 'w')
                json.dump(result_dict, f)
                f.close()

            # process.terminate()
            time.sleep(2) # time for port to be available again

    except KeyboardInterrupt:
        print('KeyboardInterrupt:', 'Interrupted')

        if args.replay:
            f = open('html_breakages.json', 'w')
            json.dump(result_dict, f)
            f.close()

        print(f"Closing any open servers")
        try:
            print(ports_list)
            for port in ports_list:
                pid = get_pid_by_port(port)
                print('pid:', pid)
                
                if pid != None:
                    os.kill(int(pid), signal.SIGINT)
                    time.sleep(2)

        except ProcessLookupError:
            print(f"No process with PID {pid1} found.")
        except PermissionError:
            print(f"Permission denied to send signal to process {pid1}.")

        try:
            # process.terminate()
            sys.exit(130)
        except SystemExit:
            os._exit(130)

    except Exception as e:
        print('Interrupted', e)

        print(f"Closing any open servers")
        try:
            print(ports_list)
            for port in ports_list:
                pid = get_pid_by_port(port)
                print(pid)
                
                if pid != None:
                    os.kill(int(pid), signal.SIGINT)
                    time.sleep(2)

        except ProcessLookupError:
            print(f"No process with PID {pid1} found.")
        except PermissionError:
            print(f"Permission denied to send signal to process {pid1}.")

        if args.replay:
            f = open('html_breakages.json', 'w')
            json.dump(result_dict, f)
            f.close()

        try:
            # process.terminate()
            sys.exit(130)
        except SystemExit:
            os._exit(130)
