#!/usr/bin/env python3
# https://stackoverflow.com/questions/3748136/how-is-cpu-usage-calculated

import os
import json
import numpy as np
import matplotlib.pyplot as plt
import sys

# list of all files in /data folder
# path = f"./docker/{args.browser}/data"
path = f"./docker/chrome/data/"
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
# dir_list = ['google.com.ar', 'twitpic.com']

data_dict = {
    'websites': [],
    'control': []
}

for extn in extn_lst:
    data_dict[extn] = []

# data_dict = {'websites': [list_of_websites], 'extn_lst[i]': [list of [usr, sys, iowait, stats]]}

faulty_sites = 0
faulty_extn = {}
for extn in extn_lst[1:]:
    faulty_extn[extn] = 0
# 'adblock': 0, 'ublock': 0, 'privacy-badger': 0

def check_for_keys(key_lst, lst):
    a = 0
    global faulty_sites
    for i in lst:
        if i not in key_lst:
            a = 1
            if i[:5] == "/data":
                faulty_sites += 1
            else:
                faulty_extn[i] += 1
            # print(lst[-1], i)
    if a:
        return False
    else:
        return True

for website in dir_list:
    f = open(path+website, 'r')
    data = json.loads(f.read())
    f.close()
    data_dict['websites'].append(website)

    # control case
    key = '/data/'+website
    
    # checking for dict key values
    extns = extn_lst[1:] 
    extns.append(key)
    check_val = check_for_keys(data['stats'].keys(), extns)

    if (check_val == False):
        continue

    try:
        usr_c = data["stats"][key]['usr']
        sys_c = data["stats"][key]['sys']
        iowait_c = data["stats"][key]['iowait']
        webStats_c = data["stats"][key]['webStats']
        data_dict['control'].append([usr_c, sys_c, iowait_c, webStats_c])
    except KeyError as k:
        print(website, k, "- dropping website")
        faulty_sites += 1
        continue

    # extn case
    for extn in extn_lst[1:]:  # opting out the 'control' case
        key = extn
        try:
            usr = data["stats"][key]['usr']
            sys = data["stats"][key]['sys']
            iowait = data["stats"][key]['iowait']
            webStats = data["stats"][key]['webStats']
            data_dict[extn].append([usr, sys, iowait, webStats])
        except KeyError as k:
            usr = usr_c
            sys = sys_c
            iowait = iowait_c
            webStats = webStats_c
            data_dict[extn].append([usr, sys, iowait, webStats])
            faulty_extn[extn] += 1
            print(website, k)
            pass

# print(data_dict)
# data_dict = {'websites':[], 'k1': [[[v1,v2,v3], [v4,v5,v6], [v1,v2,v3]], [[v1,v2,v3], [v4,v5,v6], [v1,v2,v3]]], 'k2': [[[v1,v2,v3], [v4,v5,v6], [v1,v2,v3]], [[v1,v2,v3], [v4,v5,v6], [v1,v2,v3]]], 'k3': [[[v1,v2,v3], [v4,v5,v6], [v1,v2,v3]], [[v1,v2,v3], [v4,v5,v6], [v1,v2,v3]]]}

# import sys
# print(faulty_sites)
# print(faulty_extn)
# sys.exit(0)

max_plot = [{}, {}, {}] # for usr, sys, iowait
avg_plot = [{}, {}, {}]
stat_plot = [{}, {}]

for i in range(4):
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
                    stat_plot[0][k].append(data_dict[k][i][j][0])
                    stat_plot[1][k].append(data_dict[k][i][j][1])
                else:
                    #max
                    max_plot[j][k].append(max(data_dict[k][i][j]))  

                    #avg
                    avg_plot[j][k].append(sum(data_dict[k][i][j]) / len(data_dict[k][i][j])) # can do [:-1] so that last entry can be ignored (which would mostly be close to 0) bcoz I did run mpstat for 2 extra cycle 


def sort(feature_dict):
    zipped = zip(feature_dict[extn_lst[0]], feature_dict[extn_lst[1]], feature_dict[extn_lst[2]], feature_dict[extn_lst[3]])    
    sorted_zipped = sorted(zipped)
    unzipped = list(zip(*sorted_zipped))
    for i in range(len(extn_lst)):
        feature_dict[extn_lst[i]] = list(unzipped[i])
    return feature_dict

ctrl_stat = np.array(stat_plot[0]['control'])
abp_stat = np.array(stat_plot[0]['adblock'])
ub_stat = np.array(stat_plot[0]['ublock'])

plt.plot(np.sort(abp_stat-ctrl_stat), label = 'abp')
plt.legend()
plt.show()
sys.exit(0)


# max_sort
# print(max_plot[0]['control'])
# print(sort(max_plot[0])['control'])

# for k in max_plot[0]:
# plt.plot(max_plot[0]['control'], label = 'control')
# plt.plot(max_plot[0]['adblock'], label = 'adblock')
# plt.plot(max_plot[0]['ublock'], label = 'ublock')
# plt.plot(max_plot[0]['privacy-badger'], label = 'privacy-badger')

ctrl_np = np.array(avg_plot[0]['control'])
abp_np = np.array(avg_plot[0]['adblock'])
ub_np = np.array(avg_plot[0]['ublock'])
pb_np = np.array(avg_plot[0]['privacy-badger'])

abp = [len(np.where((abp_np-ctrl_np) > 0)[0]), len(np.where((abp_np-ctrl_np) < 0)[0])]
ub = [len(np.where((ub_np-ctrl_np) > 0)[0]), len(np.where((ub_np-ctrl_np) < 0)[0])]
pb = [len(np.where((pb_np-ctrl_np) > 0)[0]), len(np.where((pb_np-ctrl_np) < 0)[0])]

print(len(ctrl_np))
print('abp[>0, <0] - ', abp)
print('ub[>0, <0] - ', ub)
print('pb[>0, <0] - ', pb)



# print(len(ctrl_np))
# print("abp:", np.average(np.sort(abp_np-ctrl_np)))
# print("ub:", np.average(np.sort(ub_np-ctrl_np)))
# print("pb:", np.average(np.sort(pb_np-ctrl_np)))


plt.plot(np.sort(abp_np), label = 'abp')
plt.legend()
plt.show()
# plt.save('lineplot.png')
