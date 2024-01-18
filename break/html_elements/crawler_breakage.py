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

from base_code import *
from Excel import *

        
extn_lst = [
     'control'
    #  , 'adblock', 'ublock', 'privacy-badger',
    #     "ghostery",
    #     "adguard"
    ]

def run(site, extn, return_dict, l, replay, temp_port1, driver_dict):
    print(site)
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

    #### MITCH
        
    for html in driver_dict.keys():
        driver_dict[html].initialize(options)

    # driver = webdriver.Chrome(options=options)
    # time.sleep(2) # wait for extension to load

        # driver_dict[html].load_site(site)
        # driver_dict[html].remove_stuff()

        if replay == 0: # can add clicking on the buttons
            # scroll
            # driver_dict[html].scroll()

            # scan + click
            try:
                url = site

                if driver_dict[html].load_site(url):
                    # driver_dict[html].remove_stuff()
                    driver_dict[html].scan_page()
                else:
                    write_noscan_row(url)
            except TimeoutException:
                write_noscan_row(driver_dict[html].url)
            except Exception as e:
                error = str(e).split("\n")[0]
                write_results([error, "N/A", "N/A", driver_dict[html].initial_outer_html, driver_dict[html].tries])

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

        driver_dict[html].close()
    vdisplay.stop()

SIZE = 10
port = 9090

#### MITCH

HTML_TEST = {'buttons', "drop downs", "links", "login"}

if __name__ == "__main__":
    # Parse the command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--replay', type=int)
    if len(sys.argv) < 2:
        parser.print_help(sys.stderr)
        sys.exit(1)
    args = parser.parse_args()

    ports_list = []
    manager = multiprocessing.Manager()
    data_dict = manager.dict()

    if args.replay == 0:
        os.system('rm -f json/*.json')

    #### MITCH

    driver_class_dict = {}
    for extn in extn_lst:
        data_dict[extn] = manager.dict()
        driver_class_dict[extn] = {}
        for html in HTML_TEST:
            data_dict[extn][html] = manager.dict()
            if not os.path.isfile(f"json/{html}_{extn}.json"):
                storeDictionary({}, html, extn)
            else:
                data_dict[extn][html] = loadDictionary(html, extn)
            driver_class_dict[extn][html] = Driver(attributes_dict[html]["attributes"], attributes_dict[html]["xpaths"], extn, html, data_dict)
            # shared_driver.initialize()
            initialize_xlsx(html, extn)

    try:
        with open("../../break/adblock_detect/inner_pages_custom_break.json", "r") as f:
            updated_dict = json.load(f)
        f.close()

        # filtering the landing pages
        websites = []
        for key in updated_dict:
            websites.append(updated_dict[key][0])
        
        websites = random.sample(websites, 1000)
        # print(websites)
        # websites = ['https://www.amazon.com', 'https://www.microsoft.com']
        
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
            print(num_chunks, chunks_list)
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
                        p1 = multiprocessing.Process(target=run, args=(chunks_list[i][j][k], extn, return_dict, multiprocessing.Lock(), args.replay, port + 2*i, driver_class_dict[extn], ))
                        jobs.append(p1)
                        
                        if i+1 != num_chunks:
                            return_dict[extn][chunks_list[i+1][j][k]] = manager.list()
                            result_dict[extn][chunks_list[i+1][j][k]] = []
                            p2 = multiprocessing.Process(target=run, args=(chunks_list[i+1][j][k], extn, return_dict, multiprocessing.Lock(), args.replay, port + 2*(i+1), driver_class_dict[extn], ))
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
    
    save_dict = {}
    for extn in extn_lst:
        save_dict[extn] = {}
        for html in HTML_TEST:
            save_dict[extn][html] = {}
            a = dict(data_dict[extn][html])
            print('-'*50)
            print(data_dict[extn][html])
            print('-'*25)
            print(a.keys())
            print('-'*50)
            # print(a)
            # for site in websites:
            #     print(a[site+'/'])
            for site in a.keys():
                save_dict[extn][html][site] = data_dict[extn][html][site]
            json.dump(a, open(f"json/{html}_{extn}.json", 'w'))
    
    json.dump(save_dict, open(f"json/master.json", 'w'))
