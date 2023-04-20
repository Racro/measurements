from detect import *
from inner_pages import *
import multiprocessing
# from tranco import Tranco
# t = Tranco(cache=True, cache_dir='.tranco')
# latest_list = t.list()
# latest_list = latest_list.top(500)

from itertools import islice

def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]

import json
import sys
import math 

with open("href_count.json", "r") as f:
    href_dict = json.load(f)
f.close()
latest_list = list(href_dict.keys())

# try_list = ["geeksforgeeks.org", "forbes.com", "insider.com"]
try_list = ["geeksforgeeks.org", "forbes.com", "insider.com"]
latest_list = try_list

extn_lst = ['adblock', 'ublock', 'privacy-badger']

SIZE = 5 # number of browser windows that will open

if __name__ == "__main__":
    updated_dict = find_inner_pages(latest_list)
    latest_list = list(updated_dict.keys())
    print(len(latest_list))
    chunks_list = list(divide_chunks(latest_list, SIZE))
    # chunks_list = [try_list]
    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    result_dict = {}
    for extn in extn_lst:       
        return_dict[extn] = manager.list()
        result_dict[extn] = []
        for i in range(math.ceil(len(chunks_list)/SIZE)):
            jobs = []
            for key in chunks_list[i]:
                # print(key)
                # return_dict[extn][key] = 0
                # print(return_dict)
                # sys.exit(0)
                # for site in updated_dict[key]:
                p = multiprocessing.Process(target=run, args=(updated_dict[key], extn, key, f, return_dict,))
                jobs.append(p)
            for job in jobs:
                job.start()

            for job in jobs:
                job.join()

        # for i in return_dict[extn]:
        #     print(i)
        for key in return_dict[extn]:
            result_dict[extn].append(key)

    print(result_dict)
    f = open("adblock_detect.json", "w")
    json.dump(result_dict, f)
    f.close()