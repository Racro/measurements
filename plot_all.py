import matplotlib.pyplot as plt
import numpy as np
import json
import sys

# def trunc(values, decs=0):
#     return np.trunc(values*10**decs)/(10**decs)

content = json.load(open('performance/data_usage/plot_content.json', 'r'))
frames = json.load(open('effective/plot_frames.json', 'r'))
performance = json.load(open('performance/cpu_load/plot_performance.json', 'r'))

# List of extensions
# extensions = ['AdBlock Plus', 'Decentraleyes', 'Disconnect', 'Ghostery', 'HTTPS Everywhere', 'NoScript Security Suite', 'Privacy Badger', 'uBlock Origin']
extensions = ['adblock', 'ublock', 'privacy-badger', "decentraleyes",
       "disconnect",
       "ghostery",
       "https",
       "noscript",
       "scriptsafe",
       "canvas-antifp",
       "adguard"]

# List of metrics
metrics = ['usr (max)', 'usr (avg)', 'sys (max)', 'sys (avg)', 'load_time', 'data_usage', '#frames']

# Sample data
data = []

for extn in extensions:
    each_extn = []
    each_extn.append(np.array(performance['usr_max'][extn]))
    each_extn.append(np.array(performance['usr_avg'][extn]))
    each_extn.append(np.array(performance['sys_max'][extn]))
    each_extn.append(np.array(performance['sys_avg'][extn]))
    each_extn.append(np.array(performance['load_time'][extn]))
    each_extn.append(np.array(performance['load_time'][extn]))
    # print(np.array(content[extn]))
    each_extn.append(np.array(content[extn]))
    each_extn.append(np.array(frames[extn]))
    data.append(each_extn)
# sys.exit(0)
# data = np.random.rand(8, 4, 20)  # now each metric has 2 values
data = np.array(data, dtype=object)

fig, axs = plt.subplots(11, 7, figsize=(20, 20))

for i, extension in enumerate(extensions):
    for j, metric in enumerate(metrics):
        if metric == '#frames':
            print(data[i, j].round(decimals=3))
        axs[i, j].plot(range(1, len(data[i, j])+1), data[i, j].round(decimals=3))  
        axs[i, j].axhline(np.percentile(data[i, j].round(decimals=3), 95), linestyle='dashed', color='g')
        if i != len(extensions) - 1:  # if not the last row
            axs[i, j].set_xticklabels([])
        if j == 0:
            axs[i, j].set_yticks([])
            axs[i, j].set_ylabel(extension, rotation='horizontal', labelpad=80, verticalalignment='center')
        if i == 0:
            axs[i, j].set_title(metric)

plt.tight_layout()
plt.show()
