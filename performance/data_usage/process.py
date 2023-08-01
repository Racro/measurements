#!/usr/bin/env python3

import os
import json
import numpy as np
import matplotlib.pyplot as plt
import sys
import json

# def trunc(values, decs=0):
#     return np.trunc(values*10**decs)/(10**decs)

# list of all files in /content folder
path = f"./data_usage2.json"

extn_lst = ['control', 'adblock', 'ublock', 'privacy-badger',
    "decentraleyes",
    "disconnect",
    "ghostery",
    "https",
    "noscript",
    "scriptsafe",
    "canvas-antifp"
    #,
    #"adguard",
    #"user-agent"
    ]

f = open(path, 'r')
data_dict = json.load(f)
f.close()

faulty_sites = {}
for extn in extn_lst:
    faulty_sites[extn] = []

def check_for_keys(): # key_lst -> list of keys in a website json object, lst -> (extn_lst + data/website)
    a = 0
    global faulty_sites
    global data_dict
    for extn in data_dict:
        for site in data_dict[extn]:
            try:
                if data_dict[extn][site] == []:
                    faulty_sites[extn].append(site)
                else:
                    if [-1,-1,-1] == data_dict[extn][site][0]:
                        if site not in faulty_sites[extn]:
                            faulty_sites[extn].append(site)

            except Exception as e:
                print(e)
                print(data_dict[extn][site])

check_for_keys()
# for extn in faulty_sites:
#     print(extn, '-', faulty_sites[extn])

# remove sites with 'control' entry
for site in faulty_sites['control']:
    for extn in extn_lst:
        del data_dict[extn][site]


# # check if keys are same for all extn
# for extn in extn_lst[1:]:
#     if list(data_dict[extn].keys()) == list(data_dict['control'].keys()):
#         print('True')
#     else:
#         print('False')

plot_data = {}
for extn in extn_lst:
    plot_data[extn] = [[], [], []]
    for site in data_dict[extn]:
        content = np.array(data_dict[extn][site], dtype=float)
        plot_data[extn][0].append(site)
        plot_data[extn][1].append((np.sum(content)*1000)/len(content))

def generate_plot_content(extn_data, ctrl_data, extn):
    ctrl_content = np.array(ctrl_data[1])
    extn_content = np.array(extn_data[1])
    websites = np.array(ctrl_data[0])

    index = np.where(extn_content == -1)
    np.delete(extn_content, index)
    np.delete(ctrl_content, index)

    zipped = zip(extn_content - ctrl_content, websites)
    sorted_zipped = sorted(zipped)
    unzipped = list(zip(*sorted_zipped))
    
    return unzipped[0]
    # print(unzipped[0])
    # plt.plot(unzipped[0], label = extn)
    # plt.axhline(np.median(unzipped[0]), linestyle='dashed', color='g')
    # plt.legend()
    # plt.show()
    # plt.savefig(f'content_{extn}.png')

# for extn in extn_lst[1:]:
ret_data = {}
for extn in extn_lst[1:]:
    # generate_plot_content(plot_data[extn], plot_data['control'], extn)
    ret_data[extn] = generate_plot_content(plot_data[extn], plot_data['control'], extn)

with open('plot_content_dummy.json', 'w') as f:
    json.dump(ret_data, f)

