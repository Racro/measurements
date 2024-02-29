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
import inspect

from base_code import *
from Excel import *
        
extn_lst = [
    # 'manual'
    'control'
    # ,
    #  'adblock'
    #  , 
    # 'ublock'
    # , 'privacy-badger'
    ]


SIZE = 10
port = 9090

HTML_TEST = {'buttons', "drop downs", "links", "login"}
# HTML_TEST = {"drop downs"}#, "links", "login"}
# HTML_TEST = {'manual'}

if __name__ == "__main__":
    # Parse the command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--replay', type=int)
    if len(sys.argv) < 2:
        parser.print_help(sys.stderr)
        sys.exit(1)
    args = parser.parse_args()

    # initial data structures
    ports_list = []
    websites = []
    manager = multiprocessing.Manager()
    data_dict = manager.dict()
    excel_dict = manager.dict()
    driver_class_dict = {}
    data_dict['errors'] = manager.dict()
    excel_dict['errors'] = manager.dict()

    # multiprocess manager to local data
    save_dict = {}
    save_excel_dict = {} 

    for extn in extn_lst:
        data_dict['errors'][extn] = manager.dict()
        excel_dict['errors'][extn] = manager.dict()

        data_dict[extn] = manager.dict()
        excel_dict[extn] = manager.dict()

        save_dict[extn] = {}
        save_excel_dict[extn] = {}

        driver_class_dict[extn] = {}
        
        for html in HTML_TEST:
            data_dict[extn][html] = manager.dict()
            excel_dict[extn][html] = manager.dict()
            excel_dict['errors'][extn][html] = manager.dict()

            save_dict[extn][html] = {}
            save_excel_dict[extn][html] = {}

            driver_class_dict[extn][html] = Driver(attributes_dict[html]["attributes"], attributes_dict[html]["xpaths"], extn, html, args.replay, data_dict, excel_dict)
             
    with open("../../break/adblock_detect/inner_pages_custom_break.json", "r") as f:
        allsite_dict = json.load(f)
    f.close()

    # filtering the landing pages
    for key in allsite_dict:
        websites.append(allsite_dict[key][0])

    if args.replay == 0:
        os.system('rm -f record_json/*.json')
        os.system('rm -f archive/*.wprgo')
        os.system('rm -rf wpr_data/*')

    # testing for 10000 sites
    websites = random.sample(websites, 10000)
    with open('websites.json', 'w') as f:
        json.dump(websites, f)
    f.close()

    # chunks_list = list(divide_chunks(websites, SIZE))
    chunks_list = list(divide_chunks(websites, SIZE))

    for extn in extn_lst:
        try: 
            folder_path = f'/home/ritik/work/pes/measurements/break/html_elements/wpr_data/{extn}'
            if not os.path.exists(folder_path):
            # Create the folder
                os.makedirs(folder_path)

            vdisplay = Display(visible=False, size=(1920, 1280))
            vdisplay.start()
            display = vdisplay.display

            num_sites = len(chunks_list[0])
            processes, ports_list = start_servers(args.replay, num_sites, extn, 0, [])
            master_port_list.append(ports_list)

            for chunk in chunks_list:
                while not check_if_ports_open(ports_list):
                    # restart all servers
                    processes, ports_list = start_servers(args.replay, num_sites, extn, 1, master_port_list[-1])
                jobs = []
                for site_index in range(len(chunk)):        
                    try:
                        p1 = multiprocessing.Process(target=run, args=(chunk[site_index], extn, args.replay, ports_list[2*site_index], ports_list[2*site_index + 1],driver_class_dict[extn], site_index, display1, ))
                        jobs.append(p1)
                    except IndexError as e:
                        error(inspect.currentframe().f_code.co_name, e)
                    except Exception as e:
                        error(inspect.currentframe().f_code.co_name, e)
                
                for job in jobs:
                    print(f"starting {job}")
                    job.start()

                time.sleep(5)

                for job in jobs:
                    print(f"joining {job}")
                    job.join(timeout = 60)

                    if job.is_alive():
                        job.terminate()

                time.sleep(2)

                if args.replay == 0:
                    for html in HTML_TEST:
                        a = dict(data_dict[extn][html])
                        for site in a.keys():
                            save_dict[extn][html][site] = data_dict[extn][html][site]

                if args.replay:
                    for html in HTML_TEST:
                        a = dict(excel_dict[extn][html])
                        for site in a.keys():
                            save_excel_dict[extn][html][site] = []
                            for elem in excel_dict[extn][html][site]:
                                save_excel_dict[extn][html][site].append(elem)

            # closing open Xfvb server
            print("-"*50)
            print("closing open xvfb processes")
            vdisplay.stop()
            # os.system('pkill Xvfb')
            print(os.system("ps aux | grep Xvfb | wc -l"))
            print("-"*50)
            
            # sleep to close the xvfb normally
            time.sleep(5)

            if args.replay == 0:
                for html in HTML_TEST:
                    json.dump(save_dict[extn][html], open(f"json/{html}_{extn}.json", 'w'))

            if args.replay:
                for html in HTML_TEST:
                    json.dump(save_excel_dict[extn][html], open(f"xlsx/{html}_{extn}.json", 'w'))

            time.sleep(2) # time for port to be available again

        except KeyboardInterrupt:
            print('KeyboardInterrupt:', 'Interrupted')
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

            if args.replay == 0:
                for html in HTML_TEST:
                    json.dump(save_dict[extn][html], open(f"json/{html}_{extn}.json", 'w'))

            if args.replay:
                for html in HTML_TEST:
                    json.dump(save_excel_dict[extn][html], open(f"xlsx/{html}_{extn}.json", 'w'))


            # try:
            #     # process.terminate()
            #     sys.exit(130)
            # except SystemExit:
            #     os._exit(130)
            pass

        except Exception as e:
            print('Interrupted:', e)

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

            if args.replay == 0:
                for html in HTML_TEST:
                    json.dump(save_dict[extn][html], open(f"json/{html}_{extn}.json", 'w'))

            if args.replay:
                for html in HTML_TEST:
                    json.dump(save_excel_dict[extn][html], open(f"xlsx/{html}_{extn}.json", 'w'))

        