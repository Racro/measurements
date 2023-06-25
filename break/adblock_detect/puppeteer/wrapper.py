import multiprocessing
# from tranco import Tranco
# t = Tranco(cache=True, cache_dir='.tranco')
# latest_list = t.list()
# latest_list = latest_list.top(500)

from bs4 import BeautifulSoup
import re 
import requests
import time

def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]

import json
import sys
import math 
import subprocess
from threading import Timer
import random
import os

# try_list = ["geeksforgeeks.org", "forbes.com", "insider.com"]
# try_list = ["geeksforgeeks.org", "forbes.com", "insider.com"]
# latest_list = try_list

extn_lst = ['adblock', 'control', 'ublock', 'privacy-badger',
       "decentraleyes",
       "disconnect",
       "ghostery",
       "https",
       "noscript",
       "scriptsafe",
       "canvas-antifp",
       "adguard",
       "user-agent"]
# extn_lst = ['']
SIZE = 15 # number of browser windows that will open

def run(sites, extn, return_dict, l):
    input_str = ""
    # random.shuffle(sites)
    for site in sites:
        input_str = input_str + site + ","
    input_str = input_str[:-1]

    fname = sites[0].split("//")[1]
    try:
        cmd = ["node", "iframes.js", input_str, extn, fname]
        # we can use "--shm-size=2g" instead of /dev/shm:/dev/shm
        process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)#, timeout = 180)

    except subprocess.TimeoutExpired as t:
        # process.kill()
        print(f'Timeout for site: {site} {extn}')
        return
    
    except subprocess.CalledProcessError as e:
        # print(e)
        # print(site, extn)
        print(f'Error for site: {site} {extn}')
        return
        # log.error(f"Error in container for '{domain}': {e.output}")
    
    stdout = process.stdout.decode('utf-8')
    stderr = process.stderr.decode('utf-8')
    print('STDOUT:', stdout) 
    print('STDERR:', stderr) 

    with open('log', 'a+') as f:
        f.write(stdout)
        f.write('\n')
        f.write(stdout)
        f.write('\n')
        f.write("-"*50)
        f.write('\n')
    f.close()

    l.acquire()
    # result_dict[extn].append(fname)
    # if stderr == "":
    #     for site in sites:
    #         return_dict[fname].append(site)
    # if stderr != "":
    #     return_dict[extn].append(fname)
    # l.release()
    if 'adblocker_detected' in stdout:
        return_dict[extn].append([stdout.split()[1], stdout.split()[3]])
    l.release()

if __name__ == "__main__":
    try:
        with open("../inner_pages_custom.json", "r") as f:
            updated_dict = json.load(f)
        f.close()
        # with open("../failed_sites.txt", "r") as f:
        #     failed_sites = f.read().splitlines()
        #     for site in failed_sites:
        #         updated_dict[site[11:]] = [site]
        # f.close()

        # updated_dict = {
        #     'geeksforgeeks.org': ['http://geeksforgeeks.org', 'https://www.geeksforgeeks.org/node-js-fs-open-method/#'],
        #     'forbes.com': ['http://forbes.com', 'https://www.forbes.com/sites/rashishrivastava/2023/04/20/ive-never-hired-a-writer-better-than-chatgpt-how-ai-is-upending-the-freelance-world/?sh=67d6db3462be', 'https://www.forbes.com/sites/digital-assets/2023/04/13/forget-art-lets-trade-how-a-10-person-startup-came-to-dominate-nft-markets/?sh=4a773f9a2680'],
        #     'hichina.com': ['http://hichina.com']
        # #     'miit.gov.cn': ['http://miit.gov.cn'],
        # #     'insider.com': ['http://insider.com', 'https://www.insider.com/renee-rapp-too-well-sex-lives-mean-girls-interview-2023-4', 'https://www.insider.com/coachella-best-female-queer-performers-you-cant-miss-2023-4']
        # #     # 'amazon.com': ['http://amazon.com', 'https://www.amazon.com/Theory-Mens-CC-Dark-Black-Multi/dp/B08SF4MP8R/']
        # }
        latest_list = list(updated_dict.keys())
        print(len(latest_list))
        chunks_list = list(divide_chunks(latest_list, SIZE))
        manager = multiprocessing.Manager()
        return_dict = manager.dict()
        result_dict = {}
        for extn in extn_lst:       
            return_dict[extn] = manager.list()
            result_dict[extn] = []
            for i in range(len(chunks_list)):
                jobs = []
                for key in chunks_list[i]:
                    p = multiprocessing.Process(target=run, args=(updated_dict[key], extn, return_dict, multiprocessing.Lock(),))
                    jobs.append(p)
                for job in jobs:
                    job.start()

                for job in jobs:
                    job.join()

            for site in return_dict[extn]:
                result_dict[extn].append(site)
            print(result_dict)
        # try: 
        #     for key in reachable_sites.keys():
        #         val = list(reachable_sites[key])
        #         if (len(val) == 0):
        #             del updated_dict[key]
        # except Exception as e:
        #     print(e)
        #     # [key]:
        #     # result_dict[key].append(site)
        
        # f = open("not_reachable_sites.json", "w")
        # json.dump(result_dict, f)
        # f.close()

        f = open("adblock_detect_custom.json", "w")
        json.dump(result_dict, f)
        f.close()
    except KeyboardInterrupt:
        print('Interrupted')
        
        f = open("adblock_detect_custom.json", "w")
        json.dump(result_dict, f)
        f.close()
        
        try:
            sys.exit(130)
        except SystemExit:
            os._exit(130)
    
