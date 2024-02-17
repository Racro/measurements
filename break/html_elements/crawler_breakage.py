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
    # 'manual'
    'control'
    ,
    #  'adblock', 
    'ublock'
    # , 'privacy-badger'
    #     "ghostery",
    #     "adguard"
    ]

def run(site, extn, return_dict, l, replay, temp_port1, driver_dict, wpr_index, display_num):
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

    # # only use when vdisplay off
    # options.add_argument("--window-size=1920,1280")

    options = remove_cmp_banner(options)
    # options = use_catapult(options, extn, temp_port1, wpr_index)

    if extn != 'control' and extn != 'manual':
        options.add_extension(f'/home/ritik/work/pes/measurements/extensions/extn_crx/{extn}.crx')
    
    # display number
    os.environ['DISPLAY'] = f":{display_num}"

    #### MITCH
    for html in driver_dict.keys():
        retval = driver_dict[html].initialize(options, 3, site)
        
        if retval == 0:
            print(f'error open browser instance for extn:{extn} and html:{html}')
            driver_dict[html] = None
            continue


    # driver = webdriver.Chrome(options=options)
    # time.sleep(2) # wait for extension to load

        # driver_dict[html].load_site(site)
        # driver_dict[html].remove_stuff()
        
        if replay == 0: # can add clicking on the buttons
            #### Manual Analysis
            if extn == 'manual':
                try:
                    url = site

                    if driver_dict[html].load_site(url):
                        # scroll
                        driver_dict[html].scroll()
                except TimeoutException as e:
                    print(f"Timeout url:{url}")
                    error = str(e).split("\n")[0]
                    print(error)
                    # write_results([error, "N/A", "N/A", driver_dict[html].url, driver_dict[html].tries])
                except Exception as e:
                    error = str(e).split("\n")[0]
                    print(error)
                    # write_results([error, "N/A", "N/A", driver_dict[html].initial_outer_html, driver_dict[html].tries])

            else:
            # scan + click
                try:
                    url = site

                    if driver_dict[html].load_site(url):
                        # driver_dict[html].remove_stuff()
                        driver_dict[html].scan_page()
                except TimeoutException as e:
                    print(f"Timeout url:{url}")
                    error = str(e).split("\n")[0]
                    print(error)
                    # write_results([error, "N/A", "N/A", driver_dict[html].url, driver_dict[html].tries])
                except Exception as e:
                    error = str(e).split("\n")[0]
                    print(error)
                    # write_results([error, "N/A", "N/A", driver_dict[html].initial_outer_html, driver_dict[html].tries])


        if replay:
            # click and compare
            tries = 1

            while driver_dict[html].curr_site > -1:
                try:
                    # print(f'curr_site: {driver_dict[html].curr_site}')
                    driver_dict[html].click_on_elms(tries)
                    # print(f'curr_site: {driver_dict[html].curr_site}')
                except Exception as e:
                    # print(e)
                    # print(site)
                    # print(driver_dict[html].url)
                    result = error_catcher(e, driver_dict[html], tries, driver_dict[html].url)
                    if type(result) is int:
                        tries = result
                    else:
                        print(driver_dict[html].url, "\t", result, driver_dict[html].initial_outer_html)
                        # write_results([result, "N/A", "N/A", driver_dict[html].initial_outer_html, tries])
                        tries = 1
                        driver_dict[html].tries = 1
                        driver_dict[html].curr_elem += 1




            # breakages = [] # list of breakages found

            # # function to test breakages
            
            # try:
            #     l.acquire()
            #     # print(fname)
            #     return_dict[extn][site].extend([breakages])
            #     l.release()
            # except Exception as e:
            #     print(e)
            #     l.release()

        driver_dict[html].close()

SIZE = 40
port = 9090

#### MITCH

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

    ports_list = []
    manager = multiprocessing.Manager()
    data_dict = manager.dict()
    excel_dict = manager.dict()

    if args.replay == 0:
        os.system('rm -f json/*.json')
        os.system('rm -f archive/*.wprgo')
        os.system('rm -rf wpr_data/*')

    with open("../../break/adblock_detect/inner_pages_custom_break.json", "r") as f:
        updated_dict = json.load(f)
    f.close()

    # filtering the landing pages
    websites = []
    for key in updated_dict:
        websites.append(updated_dict[key][0])

    if args.replay:
        websites = json.load(open('data_1000/sites.json', 'r'))
        # websites = websites[3:13]
        # websites = ['http://www.2chan.net']

    #### MITCH

    driver_class_dict = {}
    data_dict['errors'] = manager.dict()
    excel_dict['errors'] = manager.dict()
    
    for extn in extn_lst:
        data_dict['errors'][extn] = manager.dict()
        excel_dict['errors'][extn] = manager.dict()
        data_dict[extn] = manager.dict()
        excel_dict[extn] = manager.dict()

        driver_class_dict[extn] = {}
        for html in HTML_TEST:
            data_dict[extn][html] = manager.dict()
            excel_dict[extn][html] = manager.dict()
            excel_dict['errors'][extn][html] = manager.dict()

            # for website in websites:
            #     excel_dict[extn][html][website] = manager.list()
            #     excel_dict['errors'][extn][html][website] = manager.list()

            # if not os.path.isfile(f"json/{html}_{extn}.json"):
            #     storeDictionary({}, html, extn)
            # else:
            #     data_dict[extn][html] = loadDictionary(html, extn)
            driver_class_dict[extn][html] = Driver(attributes_dict[html]["attributes"], attributes_dict[html]["xpaths"], extn, html, args.replay, data_dict, excel_dict)
            # shared_driver.initialize()
            # initialize_xlsx(html, extn)

    try:
        # websites = random.sample(websites, 1000)
        # print(websites)
        # websites = ['https://www.amazon.com']#, 'https://www.microsoft.com', 'https://www.softonic.com', 'https://www.cricbuzz.com', 'https://www.nytimes.com']
        # websites = [websites[1]]
        
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
        num_chunks = len(chunks_list)
        for i in range(num_chunks):
            chunks_list[i] = list(divide_chunks(chunks_list[i], SIZE))
        print(num_chunks, chunks_list)
        
        # multiprocess
        return_dict = manager.dict()
        result_dict = {}
        save_dict = {}
        for extn in extn_lst:
            # folder_path = f'/home/ritik/work/pes/measurements/break/html_elements/wpr_data/{extn}'
            # if not os.path.exists(folder_path):
            # # Create the folder
            #     os.makedirs(folder_path)

            return_dict[extn] = manager.dict()
            result_dict[extn] = {}
            
            i = 0
            while i < num_chunks:
                # processes, pid1, pid2 = start_servers(args.replay, i, extn)
                processes, pid1, pid2 = start_servers(args.replay, i, 'control')
                if pid1 == None or pid2 == None:
                    error_code = 1
                    # break

                ports_list.append(port + 2*i)
                ports_list.append(port + 2*(i+1))
    
                error_code = 0
                for j in range(len(chunks_list[i])):        
                    print('-'*50)
                    print('j:', j)
                    jobs = []

                    vdisplay1 = Display(visible=False, size=(1920, 1280))
                    vdisplay2 = Display(visible=False, size=(1920, 1280))
                    vdisplay1.start()
                    vdisplay2.start()
                    display1 = vdisplay1.display
                    display2 = vdisplay2.display
                        
                    try:
                        for k in range(len(chunks_list[i][j])):
                            return_dict[extn][chunks_list[i][j][k]] = manager.list()
                            result_dict[extn][chunks_list[i][j][k]] = []
                            p1 = multiprocessing.Process(target=run, args=(chunks_list[i][j][k], extn, return_dict, multiprocessing.Lock(), args.replay, port + 2*i, driver_class_dict[extn], k, display1, ))
                            jobs.append(p1)
                    except IndexError as e:
                        print('crawler_breakage.py', 1, e)
                    except Exception as e:
                        print('crawler_breakage.py', 1, e)
                    
                    if i+1 != num_chunks:
                        try:
                            for k in range(len(chunks_list[i][j])):
                                return_dict[extn][chunks_list[i+1][j][k]] = manager.list()
                                result_dict[extn][chunks_list[i+1][j][k]] = []
                                p2 = multiprocessing.Process(target=run, args=(chunks_list[i+1][j][k], extn, return_dict, multiprocessing.Lock(), args.replay, port + 2*(i+1), driver_class_dict[extn], k+SIZE, display2, ))
                                jobs.append(p2)
                        except IndexError as e:
                            print('crawler_breakage.py', 1, e)
                        except Exception as e:
                            print('crawler_breakage.py', 1, e)

                    # check if any record server has stopped
                    pid1 = get_pid_by_port(port+2*i)
                    pid2 = get_pid_by_port(port+2*(i+1))
                    if pid1 == None or pid2 == None:
                        error_code = 1
                        # break
                    
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
                    print("-"*50)
                    print("closing open xvfb processes")
                    vdisplay1.stop()
                    vdisplay2.stop()
                    os.system('pkill Xvfb')
                    print(os.system("ps aux | grep Xvfb | wc -l"))
                    print("-"*50)
                
                # if error_code == 1:
                #     print(f"Found pid to be None for index: {i} and extn: {extn}")
                #     ports_list = stop_servers(i, ports_list)
                #     os.system(f'rm -f archive/{extn}_{i}.wprgo')
                #     os.system(f'rm -f archive/{extn}_{i+1}.wprgo')
                #     continue

                time.sleep(5)
                print(f"Closing opened servers with ports: {port+2*(i)} {port+2*(i+1)}")
                ports_list = stop_servers(i, ports_list)
                i = i+2
            
            if args.replay == 0:
                save_dict[extn] = {}
                for html in HTML_TEST:
                    save_dict[extn][html] = {}
                    a = dict(data_dict[extn][html])
                    for site in a.keys():
                        save_dict[extn][html][site] = data_dict[extn][html][site]
                    json.dump(a, open(f"json/{html}_{extn}.json", 'w'))

            if args.replay:
                save_dict = {}
                save_dict['errors'] = {}
                save_dict['errors'][extn] = {}
                save_dict[extn] = {}

                for html in HTML_TEST:
                    save_dict[extn][html] = {}
                    save_dict['errors'][extn][html] = {}
                    a = dict(excel_dict[extn][html])
                    for site in a.keys():
                        save_dict[extn][html][site] = []
                        save_dict['errors'][extn][html][site] = []
                        for elem in excel_dict[extn][html][site]:
                            save_dict[extn][html][site].append(elem)
                        for elem in excel_dict['errors'][extn][html][site]:
                            save_dict['errors'][extn][html][site].append(elem)    
                    json.dump(save_dict[extn][html], open(f"xlsx/{html}_{extn}.json", 'w'))

                # for site in websites:
                #     print(return_dict[extn][site])
                #     for val in return_dict[extn][site]:
                #         result_dict[extn][site].append(val)

                # f = open('html_breakages.json', 'w')
                # json.dump(result_dict, f)
                # f.close()

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

        if args.replay:
            f = open('html_breakages.json', 'w')
            json.dump(result_dict, f)
            f.close()
        
        pass

        # try:
        #     # process.terminate()
        #     sys.exit(130)
        # except SystemExit:
        #     os._exit(130)
    
    if args.replay == 0:
        save_dict = {}
        save_dict['errors'] = {}
        for extn in extn_lst:
            save_dict['errors'][extn] = {}
            save_dict['errors'][extn] = data_dict['errors'][extn].copy()
            save_dict[extn] = {}
            for html in HTML_TEST:
                save_dict[extn][html] = {}
                a = dict(data_dict[extn][html])
                # print('-'*50)
                # print(data_dict[extn][html])
                # print('-'*25)
                # print(a.keys())
                # print('-'*50)
                # print(a)
                # for site in websites:
                #     print(a[site+'/'])
                for site in a.keys():
                    save_dict[extn][html][site] = data_dict[extn][html][site]
                json.dump(a, open(f"json/{html}_{extn}.json", 'w'))
            
            json.dump(save_dict['errors'][extn], open(f"json/error_{extn}.json", 'w'))
        
        json.dump(save_dict, open(f"json/master.json", 'w'))

    if args.replay:
        save_dict = {}
        save_dict['errors'] = {}
        for extn in extn_lst:
            save_dict['errors'][extn] = {}
            save_dict[extn] = {}
            for html in HTML_TEST:
                save_dict[extn][html] = {}
                save_dict['errors'][extn][html] = {}
                a = dict(excel_dict[extn][html])

                for site in a.keys():
                    save_dict[extn][html][site] = []
                    save_dict['errors'][extn][html][site] = []

                    for elem in excel_dict[extn][html][site]:
                        save_dict[extn][html][site].append(elem)
                    for elem in excel_dict['errors'][extn][html][site]:
                        save_dict['errors'][extn][html][site].append(elem)    

                    # save_dict[extn][html][site] = excel_dict[extn][html][site]
                    # save_dict['errors'][extn][html][site] = excel_dict[extn][html][site]
                json.dump(save_dict[extn][html], open(f"xlsx/{html}_{extn}.json", 'w'))
            
            json.dump(save_dict['errors'][extn], open(f"xlsx/error_{extn}.json", 'w'))
        # print(save_dict)
        json.dump(save_dict, open(f"xlsx/master.json", 'w'))
