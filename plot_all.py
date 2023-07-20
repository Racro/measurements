import matplotlib.pyplot as plt
import numpy as np
import json
import sys
import matplotlib.patches as mpatches

content = json.load(open('performance/data_usage/plot_content.json', 'r'))
frames = json.load(open('effective/ads/plot_frames.json', 'r'))
performance = json.load(open('performance/cpu_load/plot_performance.json', 'r'))
third_party = json.load(open('effective/third_party/plot_third_party.json', 'r'))
ram = json.load(open('performance/cpu_load/plot_ram.json', 'r'))
jsheap = json.load(open('performance/cpu_load/plot_jsheap.json', 'r'))

# List of extensions
# extensions = ['AdBlock Plus', 'Decentraleyes', 'Disconnect', 'Ghostery', 'HTTPS Everywhere', 'NoScript Security Suite', 'Privacy Badger', 'uBlock Origin']
extensions = ['adblock', 'ublock', 'privacy-badger', "decentraleyes",
       "disconnect",
       "ghostery",
       "https",
       "noscript",
       "scriptsafe",
       "canvas-antifp",
       "adguard",
       "user-agent"]

extn_dict = {
    'adblock': 'ABP', 'ublock': 'UbO', 'privacy-badger': 'PB', "decentraleyes": 'Decentraleyes',
       "disconnect": 'Disconnect',
       "ghostery": 'Ghostery',
       "https": 'HTTPS Everywhere',
       "noscript": 'NoScript',
       "scriptsafe": 'ScriptSafe',
       "canvas-antifp": 'CFD',
       "adguard": 'AdG',
       "user-agent": 'UA Switcher'
}

# List of metrics
metrics = ['usr (max)\n(in absolute)', 'usr (avg)\n(in absolute)', 'sys (max)\n(in absolute)', 'sys (avg)\n(in absolute)', 'load_time\n(in seconds)', 'data_usage\n(in MB)', 'RAM_usage_max\n(in MB)', 'RAM_usage_avg\n(in MB)', 'JSHeapSizeUsed\n(in MB)']
# metrics = ['load_time\n(in seconds)', 'data_usage\n(in MB)']

# Sample data
data = []

for extn in extensions:
    each_extn = []
    each_extn.append(np.array(performance['usr_max'][extn]))
    each_extn.append(np.array(performance['usr_avg'][extn]))
    each_extn.append(np.array(performance['sys_max'][extn]))
    each_extn.append(np.array(performance['sys_avg'][extn]))
    each_extn.append(np.array(performance['load_time'][extn]))
    # print(np.array(content[extn]))
    each_extn.append(np.array(content[extn]))
    each_extn.append(np.array(ram['ram_max'][extn]))
    each_extn.append(np.array(ram['ram_avg'][extn]))
    each_extn.append(np.array(jsheap['jsheap'][extn]))
    # each_extn.append(np.array(frames[extn]))
    # each_extn.append(np.array(third_party[extn]))
    data.append(each_extn)
# sys.exit(0)
# data = np.random.rand(8, 4, 20)  # now each metric has 2 values
data = np.array(data, dtype=object)

fig, axs = plt.subplots(12, 9, figsize=(20, 20))
# plt.subplots_adjust(bottom=0.02, right=1)
# axs = axs.transpose()

perc_95 = {}
perc_50 = {}
perc_99 = {}
avg = {}
mad = {}
mr = {}
std = {}

for extn in extensions:
    perc_50[extn] = []
    perc_95[extn] = []
    perc_99[extn] = []
    avg[extn] = []
    mad[extn] = []
    std[extn] = []

# Blue Shades
blue_shades = ['#aed6f1', '#85c1e9', '#3498db']

# Red Shades
red_shades = ['#f5b7b1', '#f1948a', '#e74c3c']

max_min = [[], []]

for j, metric in enumerate(metrics):
    max_min[0].append(0)
    max_min[1].append(0)

for j, metric in enumerate(metrics):
    min_val = 10000
    max_val = 0
    for i, extension in enumerate(extensions):
        min_val = min(min(data[i,j]), min_val)    
        max_val = max(max(data[i,j]), max_val)    
    max_min[0][j] = max_val
    max_min[1][j] = min_val

for i, extension in enumerate(extensions):
    for j, metric in enumerate(metrics):

        # just for analysis
        mean = np.round(np.average(data[i, j]), 3)
        med = np.round(np.percentile(data[i, j], 50), 3)
        mad_local = np.round(np.median(np.absolute(data[i, j] - np.median(data[i, j]))), 3)
        std_local = np.round(np.std(data[i, j]), 3)

        perc_95[extension].append(np.round(np.percentile(data[i, j], 95), 3))
        perc_50[extension].append(med)
        # perc_99[extension].append(np.round(np.percentile(data[i, j], 99), 3))
        avg[extension].append(mean)
        mad[extension].append(mad_local)
        std[extension].append(std_local)

        axs[i, j].plot(np.round(data[i, j], 3), range(len(data[i, j])), color="black")
        if j < 9:
            axs[i, j].axvline(np.round(np.percentile(data[i, j], 50), 3), linestyle='dashed', color='g')
            
            # Set the face color of the subplot
            if med < -2.5*mad_local:
                axs[i, j].set_facecolor(blue_shades[2])
            elif -2.5*mad_local <= med and med < -1.5*mad_local:
                axs[i, j].set_facecolor(blue_shades[1])
            elif -1.5*mad_local <= med and med < -0.5*mad_local:
                axs[i, j].set_facecolor(blue_shades[0])
            elif -0.5*mad_local <= med and med < 0.5*mad_local:
                axs[i, j].set_facecolor('#ffffff')
            elif 0.5*mad_local <= med and med < 1.5*mad_local:
                axs[i, j].set_facecolor(red_shades[0])
            elif 1.5*mad_local <= med and med < 2.5*mad_local:
                axs[i, j].set_facecolor(red_shades[1])
            elif med >= 2.5*mad_local:
                axs[i, j].set_facecolor(red_shades[2])
            else:
                print("ERRROR")

            # if med < -1.5*mad_local:
            #     axs[i, j].set_facecolor(blue_shades[2])
            # elif -1.5*mad_local <= med and med < -0.5*mad_local:
            #     axs[i, j].set_facecolor(blue_shades[1])
            # elif -0.5*mad_local <= med and med < -0.25*mad_local:
            #     axs[i, j].set_facecolor(blue_shades[0])
            # elif -0.25*mad_local <= med and med < 0.25*mad_local:
            #     axs[i, j].set_facecolor('#ffffff')
            # elif 0.25*mad_local <= med and med < 0.5*mad_local:
            #     axs[i, j].set_facecolor(red_shades[0])
            # elif 0.5*mad_local <= med and med < 1.5*mad_local:
            #     axs[i, j].set_facecolor(red_shades[1])
            # elif med >= 1.5*mad_local:
            #     axs[i, j].set_facecolor(red_shades[2])
            # else:
            #     print("ERRROR")
        else:
            axs[i, j].axhline(np.round(np.average(data[i, j]), 3), linestyle='dashed', color='g')

            # Set the face color of the subplot
            # if mean < -2.5*std_local:
            #     axs[i, j].set_facecolor(blue_shades[2])
            # elif -2.5*std_local <= mean and mean < -1.5*std_local:
            #     axs[i, j].set_facecolor(blue_shades[1])
            # elif -1.5*std_local <= mean and mean < -0.5*std_local:
            #     axs[i, j].set_facecolor(blue_shades[0])
            # elif -0.5*std_local <= mean and mean < 0.5*std_local:
            #     axs[i, j].set_facecolor('#ffffff')
            # elif 0.5*std_local <= mean and mean < 1.5*std_local:
            #     axs[i, j].set_facecolor(red_shades[0])
            # elif 1.5*std_local <= mean and mean < 2.5*std_local:
            #     axs[i, j].set_facecolor(red_shades[1])
            # elif mean >= 2.5*std_local:
            #     axs[i, j].set_facecolor(red_shades[2])
            # else:
            #     print("ERRROR")

            if mean < -1.5*std_local:
                axs[i, j].set_facecolor(blue_shades[2])
            elif -1.5*std_local <= mean and mean < -0.5*std_local:
                axs[i, j].set_facecolor(blue_shades[1])
            elif -0.5*std_local <= mean and mean < -0.25*std_local:
                axs[i, j].set_facecolor(blue_shades[0])
            elif -0.25*std_local <= mean and mean < 0.25*std_local:
                axs[i, j].set_facecolor('#ffffff')
            elif 0.25*std_local <= mean and mean < 0.5*std_local:
                axs[i, j].set_facecolor(red_shades[0])
            elif 0.5*std_local <= mean and mean < 1.5*std_local:
                axs[i, j].set_facecolor(red_shades[1])
            elif mean >= 1.5*std_local:
                axs[i, j].set_facecolor(red_shades[2])
            else:
                print("ERRROR")

        # set tick positions on y-axis
        y = [0, int(len(data[i, j])/2), len(data[i, j])]
        tick_positions = [0, 0.5, 1]
        axs[i, j].set_yticks(y)
        axs[i, j].set_yticklabels(tick_positions)

        # val = np.round(max(max(data[i,j]), abs(min(data[i,j]))), -3) 
        x = [max_min[1][j], 0, max_min[0][j]]
        # tick_positions = [0, 0.5, 1]
        axs[i, j].set_xticks(x)
        # axs[i, j].set_yticklabels(tick_positions)

        if j > 0:
            axs[i, j].set_yticklabels([])
        if i != len(extensions) - 1:  # if not the last row
            axs[i, j].set_xticklabels([])
        if j == 0:
            # axs[i, j].set_yticks([])
            axs[i, j].set_ylabel(extn_dict[extension], rotation='horizontal', labelpad=80, verticalalignment='center')
        if i == 0:
            axs[i, j].set_title(metric, weight='bold')

#legend
x_tilde = '\u0078\u0303'
goe = '\u2265'
loe = '\u2264'
x_bar = 'x'+'\u0305'
sigma = '\u03C3'

text = mpatches.Patch(facecolor='#ffffff', label='Performance: ')
blue_patch1 = mpatches.Patch(facecolor=blue_shades[2], label=f'{x_tilde} < -2.5M',  edgecolor='black')
blue_patch2 = mpatches.Patch(facecolor=blue_shades[1], label=f'-2.5M {loe} {x_tilde} < -1.5M',  edgecolor='black')
blue_patch3 = mpatches.Patch(facecolor=blue_shades[0], label=f'-1.5M {loe} {x_tilde} < -0.5M',  edgecolor='black')
white_patch = mpatches.Patch(facecolor='#ffffff', label=f'-0.5M {loe} {x_tilde} < 0.5M',  edgecolor='black')
red_patch1 = mpatches.Patch(facecolor=red_shades[0], label=f'0.5M {loe} {x_tilde} < 1.5M',  edgecolor='black')
red_patch2 = mpatches.Patch(facecolor=red_shades[1], label=f'1.5M {loe} {x_tilde} < 2.5M',  edgecolor='black')
red_patch3 = mpatches.Patch(facecolor=red_shades[2], label=f'{x_tilde} {goe} 2.5M',  edgecolor='black')

# text = mpatches.Patch(facecolor='#ffffff', label='Effectiveness: ')
# blue_patch1 = mpatches.Patch(facecolor=blue_shades[2], label=f'{x_bar} < -1.5{sigma}',  edgecolor='black')
# blue_patch2 = mpatches.Patch(facecolor=blue_shades[1], label=f'-1.5{sigma} {loe} {x_bar} < -0.5{sigma}',  edgecolor='black')
# blue_patch3 = mpatches.Patch(facecolor=blue_shades[0], label=f'-0.5{sigma} {loe} {x_bar} < -0.25{sigma}',  edgecolor='black')
# white_patch = mpatches.Patch(facecolor='#ffffff', label=f'-0.25{sigma} {loe} {x_bar} < 0.25{sigma}',  edgecolor='black')
# red_patch1 = mpatches.Patch(facecolor=red_shades[0], label=f'0.25{sigma} {loe} {x_bar} < 0.5{sigma}',  edgecolor='black')
# red_patch2 = mpatches.Patch(facecolor=red_shades[1], label=f'0.5{sigma} {loe} {x_bar} < 1.5{sigma}',  edgecolor='black')
# red_patch3 = mpatches.Patch(facecolor=red_shades[2], label=f'{x_bar} {goe} 1.5{sigma}',  edgecolor='black')

# legend = plt.legend(handles=[text, blue_patch1, blue_patch2, blue_patch3, white_patch, red_patch1, red_patch2, red_patch3], loc='lower center', bbox_to_anchor=(0, -1.5), ncol=8)

plt.tight_layout()
plt.show()

# print(f'perc_50: {perc_50}')
# print(f'perc_95: {perc_95}')
# # print(f'perc_99: {perc_99}')
# print(f'avg: {avg}')
# print(f'mad: {mad}')
# print(f'std: {std}')