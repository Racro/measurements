#!/usr/bin/env python3
# https://stackoverflow.com/questions/3748136/how-is-cpu-usage-calculated

import os
import json
import numpy as np
import matplotlib.pyplot as plt
import sys

# list of all files in /data folder
path = f"./data_1000/data_custom/"
dir_list = os.listdir(path)
# dir_list = dir_list[:6000]

# extn_lst = ['control', 'adblock', 'ublock', 'privacy-badger']
extn_lst = ['control', 'adblock', 'ublock', 'privacy-badger',
       "decentraleyes",
       "disconnect",
       "ghostery",
       "https",
       "noscript",
       "scriptsafe",
       "canvas-antifp",
       "adguard"]

data_dict = {
    'websites': []
}

for extn in extn_lst:
    data_dict[extn] = [] # data_dict = {'websites': [list_of_websites], 'extn_lst[i]': [list of [usr, sys, iowait, stats]]}

faulty_sites = 0
faulty_extn = {}
for extn in extn_lst[1:]:
    faulty_extn[extn] = 0

def check_for_keys(key_lst, lst): # key_lst -> list of keys in a website json object, lst -> (extn_lst + data/website)
    a = 0
    global faulty_sites
    faulty_lst = []
    for i in lst:
        if i not in key_lst:
            a = 1
            if i[:5] == "/data":
                faulty_sites += 1
                faulty_lst = []
                break
            else:
                faulty_extn[i] += 1
                faulty_lst.append(i)
    if a:
        return False, faulty_lst
    else:
        return True, faulty_lst

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


for website in dir_list:
    f = open(path+website, 'r')
    data = json.load(f)
    f.close()

    # control case
    key = '/data/'+website
    
    # checking for dict key values
    extns = extn_lst[1:] 
    extns.append(key)
    check_val, faulty_lst = check_for_keys(data['stats'].keys(), extns)

    if (check_val == False):
        print("----------------- check this -------------------")
        if faulty_lst != []:
            for extn in faulty_lst:
                data["stats"][extn] = {"webStats": [-1, -1]}
        else:
            print(website)
            continue # only continue in ctrl case not found
    data_dict['websites'].append(website)

    try:
        usr_c = data["stats"][key]['usr']
        sys_c = data["stats"][key]['sys']
        iowait_c = data["stats"][key]['iowait']
        webStats_c = data["stats"][key]['webStats']
        data_dict['control'].append([usr_c, sys_c, iowait_c, webStats_c])
    except KeyError as k:
        print(website, k, "- dropping website")
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
            faulty_extn[extn] += 1
            print(website, k)
            pass

# print(data_dict)
# data_dict = {'websites':[], 'k1': [[[v1,v2,v3,ws1], [v4,v5,v6,ws2], [v1,v2,v3,ws3]], [[v1,v2,v3,ws11], [v4,v5,v6,ws21], [v1,v2,v3, ws31]]], 'k2': [[[v1,v2,v3], [v4,v5,v6], [v1,v2,v3]], [[v1,v2,v3], [v4,v5,v6], [v1,v2,v3]]], 'k3': [[[v1,v2,v3], [v4,v5,v6], [v1,v2,v3]], [[v1,v2,v3], [v4,v5,v6], [v1,v2,v3]]]}

max_plot = [{}, {}, {}] # for usr, sys, iowait
avg_plot = [{}, {}, {}]
stat_plot = [{}, {}]

for i in range(4): # initialization
    for k in data_dict:
        if k != 'websites':
            if (i == 3):
                stat_plot[0][k] = []
                stat_plot[1][k] = []
            else:
                max_plot[i][k] = []
                avg_plot[i][k] = []
            
for i in range(len(data_dict['control'])):
    for k in data_dict:
        for j in range(4):
            if k != 'websites':
                if (j==3):
                    # # filter out -1 values from stat_plot
                    # if data_dict[k][i][j][0] == -1 or data_dict[k][i][j][1] == -1:
                    #     continue 

                    stat_plot[0][k].append(data_dict[k][i][j][0])
                    stat_plot[1][k].append(data_dict[k][i][j][1])
                else:
                    #max
                    max_plot[j][k].append(max(data_dict[k][i][j]))  

                    #avg
                    avg_plot[j][k].append(sum(data_dict[k][i][j]) / len(data_dict[k][i][j])) # can do [:-1] so that last entry can be ignored (which would mostly be close to 0) bcoz I did run mpstat for 2 extra cycle 

def generate_stats_dict(data_dict):
    websites = np.array(data_dict['websites'])
    # extn_stat = []
    dele = {}
    d = {}
    for extn in extn_lst:
        if extn == 'control':
            continue

        # extn_stat.append(np.array(stat_plot[1][extn]))
        dele[extn] = np.array(stat_plot[1][extn])
        d[extn] = {}

        # filter all -1 values from stat_plot
        dummy = np.array(stat_plot[1]['control'])
        index = np.where(dele[extn] == -1)
        # print(index)
        # print(dele[extn][index])
        # print(dummy[index])
        # print(websites[index])
        np.delete(dele[extn], index)
        np.delete(dummy, index)
        zipped = zip(dele[extn] - dummy, websites)
        sorted_zipped = sorted(zipped)
        unzipped = list(zip(*sorted_zipped))
        x = list(unzipped[1])
        y = list(unzipped[0])
        for j in range(len(x)):
            d[extn][x[j]] = y[j]
    
    import json
    with open('website_categorization/site_load_time_custom_1000.json', 'w') as f:
        json.dump(d, f, cls=NpEncoder)
    f.close()
generate_stats_dict(data_dict)


# plt.axhline(np.mean(ub_stat-ctrl_stat), linestyle='dashed', color='g')
sys.exit(0)

avg_np = {}
max_np = {}
for extn in extn_lst:
    avg_np[extn] = np.array(avg_plot[0][extn])
    max_np[extn] = np.array(max_plot[0][extn])

def plot_max():
    for extn in max_np.keys():
        if extn != 'control':
            plt.plot(np.sort(max_np[extn] - max_np['control']), label = extn)
            plt.legend()
            plt.savefig(f'max_{extn}.png')

def plot_avg():
    for extn in avg_np.keys():
        if extn != 'control':
            plt.plot(np.sort(avg_np[extn] - avg_np['control']), label = extn)
            plt.legend()
            plt.savefig(f'avg_{extn}.png')

# print("abp:", np.average(np.sort(abp_np-ctrl_np)))
# abp = [len(np.where((abp_np-ctrl_np) > 0)[0]), len(np.where((abp_np-ctrl_np) < 0)[0])]




# plt.show()
# plt.save('lineplot.png')
