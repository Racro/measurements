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
import os

extn_lst = ['control', 'adblock', 'ublock', 'privacy-badger']

SIZE = 10 # number of browser windows that will open

def run(sites, extn, return_dict, l):
    input_str = ""
    for site in sites:
        input_str = input_str + site + ","
    input_str = input_str[:-1]

    fname = sites[0].split("//")[1]
    if fname[:3] == 'www':
        fname = fname[4:]

    for i in range(3):
        try:
            cmd = ["node", "content.js", input_str, extn, fname]
            process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)#, timeout = 180)

        except subprocess.TimeoutExpired as t:
            print(f'Timeout for site: {site} {extn}')
            return
        
        except subprocess.CalledProcessError as e:
            print(f'Error for site: {site} {extn}')
            return
        
        stdout = process.stdout.decode('utf-8')
        stderr = process.stderr.decode('utf-8')
        print('STDOUT:', stdout) 
        print('STDERR:', stderr)
        with open('log', 'w') as f:
            f.write(f'STDOUT: {stdout}\n') 
            f.write(f'STDERR: {stderr}\n')
        f.close() 
        
        try:
            l.acquire()
            print(fname)
            if stderr == "":
                return_dict[extn][fname].append(format(float(stdout.split()[2]), '.2f'))
            else:
                return_dict[extn][fname].append(-1)
            l.release()
        except Exception as e:
            print(2222)
            print(e)
            l.release()
    # if 'adblocker_detected' in stdout:
    #     return_dict[extn].append(stdout.split()[1])

if __name__ == "__main__":
    try:
        with open("../../adblock_detect/inner_pages.json", "r") as f:
            updated_dict = json.load(f)
        f.close()
        # updated_dict = {
        #     "google.com": ["http://www.google.com"]
        #     # ,
        #     # "youtube.com": ["http://www.youtube.com"]
        #     # 'geeksforgeeks.org': ['http://geeksforgeeks.org', 'https://www.geeksforgeeks.org/node-js-fs-open-method/#']#,
        #     # 'forbes.com': ['http://forbes.com', 'https://www.forbes.com/sites/rashishrivastava/2023/04/20/ive-never-hired-a-writer-better-than-chatgpt-how-ai-is-upending-the-freelance-world/?sh=67d6db3462be', 'https://www.forbes.com/sites/digital-assets/2023/04/13/forget-art-lets-trade-how-a-10-person-startup-came-to-dominate-nft-markets/?sh=4a773f9a2680']
        #     # 'hichina.com': ['http://hichina.com'],
        #     # 'miit.gov.cn': ['http://miit.gov.cn']
        #     # 'insider.com': ['http://insider.com', 'https://www.insider.com/renee-rapp-too-well-sex-lives-mean-girls-interview-2023-4', 'https://www.insider.com/coachella-best-female-queer-performers-you-cant-miss-2023-4'],
        #     # 'amazon.com': ['http://amazon.com', 'https://www.amazon.com/Theory-Mens-CC-Dark-Black-Multi/dp/B08SF4MP8R/']
        # }
        latest_list = list(updated_dict.keys())
        print(len(latest_list))
        chunks_list = list(divide_chunks(latest_list, SIZE))
        manager = multiprocessing.Manager()
        return_dict = manager.dict()
        result_dict = {}
        for extn in extn_lst:       
            return_dict[extn] = manager.dict()
            result_dict[extn] = {}
            for i in range(len(chunks_list)):
                jobs = []
                for key in chunks_list[i]:
                    return_dict[extn][key] = manager.list()
                    result_dict[extn][key] = []
                    p = multiprocessing.Process(target=run, args=(updated_dict[key], extn, return_dict, multiprocessing.Lock(),))
                    jobs.append(p)
                for job in jobs:
                    job.start()

                for job in jobs:
                    job.join()
            
            for site in latest_list:
                print(return_dict[extn][site])
                for val in return_dict[extn][site]:
                    result_dict[extn][site].append(val)

        f = open('data_usage.json', 'w')
        json.dump(result_dict, f)
        f.close()

    except KeyboardInterrupt:
        print('Interrupted')

        f = open('data_usage.json', 'w')
        json.dump(result_dict, f)
        f.close()

        try:
            sys.exit(130)
        except SystemExit:
            os._exit(130)
    