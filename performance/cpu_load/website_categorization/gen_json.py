#!/usr/bin/env python3
# https://stackoverflow.com/questions/3748136/how-is-cpu-usage-calculated

import os
import json
import numpy as np
import matplotlib.pyplot as plt
import sys

# def trunc(values, decs=0):
#     return np.trunc(values*10**decs)/(10**decs)

def sort(feature_dict):
    zipped = zip(feature_dict[extn_lst[0]], feature_dict[extn_lst[1]], feature_dict[extn_lst[2]], feature_dict[extn_lst[3]])    
    sorted_zipped = sorted(zipped)
    unzipped = list(zip(*sorted_zipped))
    for i in range(len(extn_lst)):
        feature_dict[extn_lst[i]] = list(unzipped[i])
    return feature_dict

class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NpEncoder, self).default(obj)

def generate_stats_dict(data_dict):
    websites = np.array(data_dict['websites'])
    # extn_stat = []
    dele = {}
    d = {}

    ret = {}
    for extn in extn_lst:
        if extn == 'control':
            continue

        # extn_stat.append(np.array(stat_plot[1][extn]))
        dele[extn] = np.array(stat_plot[1][extn])
        d[extn] = {}

        # filter all -1 values from stat_plot
        dummy = np.array(stat_plot[1]['control'])
        index = np.where(dele[extn] == -1)

        np.delete(dele[extn], index)
        np.delete(dummy, index)
        zipped = zip(dele[extn] - dummy, websites)
        sorted_zipped = sorted(zipped)
        unzipped = list(zip(*sorted_zipped))
        x = list(unzipped[1]) # x -> website
        y = list(unzipped[0]) # y -> extn_time - ctrl_time
        
        ret[extn] = np.sort(np.array(y))

        for j in range(len(x)):
            d[extn][x[j]] = y[j]


        # # plot
        # plt.plot(np.sort(np.array(y)), label = extn)
        # plt.axhline(np.median(np.array(y)), linestyle='dashed', color='g')
        # plt.legend()
        # plt.show()
        # # plt.savefig(f'stat_{extn}.png')
    return d
    # import json
    # with open('website_categorization/site_load_time_custom_1000.json', 'w') as f:
    #     json.dump(d, f, cls=NpEncoder)
    # f.close()

# list of all files in /data folder
path = f"./../data_1000/data_custom/"
dir_list = os.listdir(path)

# extn_lst = ['control', 'adblock', 'ublock', 'privacy-badger']
extn_lst = [
    'control', 'adblock', 'ublock', 'privacy-badger',
       "decentraleyes",
       "disconnect",
       "ghostery",
       "https",
       "noscript",
       "scriptsafe",
       "canvas-antifp",
       "adguard",
       "user-agent"]

data_dict = {
    'websites': []
}

for extn in extn_lst:
    data_dict[extn] = [] # data_dict = {'websites': [list_of_websites], 'extn_lst[i]': [list of [usr, sys, iowait, stats]]}

faulty_sites = {}
# faulty_extn = {}
for extn in extn_lst:
    faulty_sites[extn] = []

def check_for_keys(website_data, website): 
    # website_data -> data dict of each website, website -> website
    global faulty_sites
    for extn in extn_lst:
        if extn == 'control':
            if f'/data/{website}' not in website_data.keys():
                faulty_sites[extn].append(website)
        else:
            if extn not in website_data.keys():
                faulty_sites[extn].append(website)

# load all the data from the files in 1 dictionary
all_data = {}
for website in dir_list:
    f = open(path+website, 'r')
    data = json.load(f)
    f.close()
    all_data[website] = data

# populate the faulty_sites dict
for website in all_data:
    check_for_keys(all_data[website]['stats'], website)

faulty_num = {}
for extn in extn_lst[1:]:
    faulty_num[extn] = 0

for website in dir_list:
    # control case
    key = '/data/'+website
    data = all_data[website]

    if website in faulty_sites['control']:
        continue
    for extn in extn_lst[1:]:
        if website in faulty_sites[extn]:
            data["stats"][extn] = {"webStats": [-1, -1]}

    data_dict['websites'].append(website)

    try:
        usr_c = data["stats"][key]['usr']
        sys_c = data["stats"][key]['sys']
        iowait_c = data["stats"][key]['iowait']
        webStats_c = data["stats"][key]['webStats']
        data_dict['control'].append([usr_c, sys_c, iowait_c, webStats_c])
    except KeyError as k:
        # print(website, k, "- dropping website")
        faulty_sites += 1
        data_dict['websites'] = data_dict['websites'][:-1]
        continue

    # extn case
    for extn in extn_lst[1:]:  # opting out the 'control' case
        key = extn
        try:
            usr = data["stats"][key]['usr']
            syst = data["stats"][key]['sys']
            iowait = data["stats"][key]['iowait']
            webStats = data["stats"][key]['webStats']
            data_dict[extn].append([usr, syst, iowait, webStats])
        except KeyError as k:
            usr = usr_c
            syst = sys_c
            iowait = iowait_c
            webStats = webStats_c
            data_dict[extn].append([usr, syst, iowait, webStats])
            faulty_num[extn] += 1
            print(website, extn,  k)
            pass

print(faulty_num) # manually removed the 0.0 extries corresponding to the number here

# data_dict = {'websites':[], 'k1': [[[v1,v2,v3,ws1], [v4,v5,v6,ws2], [v1,v2,v3,ws3]], [[v1,v2,v3,ws11], [v4,v5,v6,ws21], [v1,v2,v3, ws31]]], 'k2': [[[v1,v2,v3], [v4,v5,v6], [v1,v2,v3]], [[v1,v2,v3], [v4,v5,v6], [v1,v2,v3]]], 'k3': [[[v1,v2,v3], [v4,v5,v6], [v1,v2,v3]], [[v1,v2,v3], [v4,v5,v6], [v1,v2,v3]]]}

max_plot = [{}, {}, {}] # for usr, sys, iowait
avg_plot = [{}, {}, {}]
stat_plot = [{}, {}]

for i in range(4): # initialization
    for extn in data_dict:
        if extn != 'websites':
            if (i == 3):
                stat_plot[0][extn] = []
                stat_plot[1][extn] = []
            else:
                max_plot[i][extn] = []
                avg_plot[i][extn] = []
            
for i in range(len(data_dict['control'])):
    for extn in data_dict:
        for j in range(4):
            if extn != 'websites':
                if (j==3):
                    # # filter out -1 values from stat_plot
                    # if data_dict[extn][i][j][0] == -1 or data_dict[extn][i][j][1] == -1:
                    #     continue

                    stat_plot[0][extn].append(data_dict[extn][i][j][0])
                    stat_plot[1][extn].append(data_dict[extn][i][j][1])
                else:
                    #max
                    max_plot[j][extn].append(max(data_dict[extn][i][j]))  

                    #avg
                    avg_plot[j][extn].append(sum(data_dict[extn][i][j][:-3]) / len(data_dict[extn][i][j][:-3])) # can do [:-1] so that last entry can be ignored (which would mostly be close to 0) bcoz I did run mpstat for 5 extra cycle 


ret_data = generate_stats_dict(data_dict)

json.dump(ret_data, open('site_load_time_custom2_1000.json', 'w'), cls=NpEncoder)
