#!/usr/bin/env python3

import os
import json
import numpy as np
import matplotlib.pyplot as plt
import sys
import json

class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NpEncoder, self).default(obj)

# def trunc(values, decs=0):
#     return np.trunc(values*10**decs)/(10**decs)

# list of all files in /frames folder
path = f"./third_party_data.json"
f = open(path, 'r')
data_dict = json.load(f)
f.close()

f = open('./../../gen_sites/test_sites_custom.txt', 'r')
urls = f.read().splitlines()
f.close()

extn_lst = ['control', 'adblock', 'ublock', 'privacy-badger',
    "decentraleyes",
    "disconnect",
    "ghostery",
    "https",
    "noscript",
    "scriptsafe",
    "canvas-antifp",
    "adguard",
    "user-agent"]

faulty_sites = {}
for extn in extn_lst:
    faulty_sites[extn] = []

def check_for_keys(): # key_lst -> list of keys in a website json object, lst -> (extn_lst + data/website)
    global faulty_sites
    global data_dict

    faulty_urls = list(set(urls) - set(list(data_dict['control'].keys())))

    for site in faulty_urls:
        for extn in extn_lst[1:]:
            del data_dict[extn][site]

check_for_keys()

plot_data = {}
for extn in extn_lst:
    plot_data[extn] = [[], []]
    for site in data_dict[extn]:
        try:
            plot_data[extn][1].append(data_dict[extn][site] - data_dict['control'][site])
        except Exception as e:
            print(e)
            continue
        plot_data[extn][0].append(site)

def generate_plot_third_party(extn_data, extn):
    extn_frames = np.array(extn_data[1]) # 2 for docs
    websites = np.array(extn_data[0])

    zipped = zip(extn_frames, websites)
    sorted_zipped = sorted(zipped)
    unzipped = list(zip(*sorted_zipped))
    
    return unzipped[0]

# for extn in extn_lst[1:]:
ret_data = {}
for extn in extn_lst[1:]:
    # generate_plot_frames(plot_data[extn], plot_data['control'], extn)
    ret_data[extn] = generate_plot_third_party(plot_data[extn], extn)

with open('plot_third_party.json', 'w') as f:
    json.dump(ret_data, f, cls=NpEncoder)
f.close()