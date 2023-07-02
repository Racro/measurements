import os
import json 

path = "./../performance/cpu_load/data_1000/data_custom/"
dir_list = os.listdir(path)

extn_lst = [
    # Extensions on their own
    "adblock",
    "decentraleyes",
    "disconnect",
    "ghostery",
    "https",
    "noscript",
    "privacy-badger",
    "ublock",
    "scriptsafe",
    "canvas-antifp",
    "adguard",
    "user-agent"  
]

hang = {}

for extn in extn_lst:
    hang[extn] = 0

count = 0
for file in dir_list:
    f = open(path+file, 'r')
    d = json.load(f)
    keys = d['stats'].keys()
    # print(keys)
    # sys.exit()
    ctrl = f'/data/{file}'
    if ctrl not in keys:
        count += 1
        continue
    else:
        for extn in extn_lst:
            if extn not in keys:
                hang[extn] += 1

print(count)
for extn in hang:
    print(f'{extn}: {hang[extn]}')