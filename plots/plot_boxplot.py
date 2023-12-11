import matplotlib.pyplot as plt
import numpy as np
import json

# Define the number of extensions, metrics, and the width of each boxplot and the gap between groups of boxplots
num_extensions = 7
num_metrics = 3
# Let's increase the width of the boxplots and decrease the spacing between them
box_width = 0.9  # Increase the width of the boxplots

# Define the gap between the boxplots within the same metric
gap_within_metric = 0.2

metric_spacing = 0.8  # Increase the spacing between metrics

# Define the number of metrics in each row
num_metrics_1 = 3
# num_metrics_2 = 2
# num_metrics_3 = 2

# List of extensions
# extensions = ['AdBlock Plus', 'Decentraleyes', 'Disconnect', 'Ghostery', 'HTTPS Everywhere', 'NoScript Security Suite', 'Privacy Badger', 'uBlock Origin']
extensions = ['adblock'
              , 'ublock', 'privacy-badger', "decentraleyes",
       "disconnect",
       "ghostery",
    #    "https",
    #    "noscript",
    #    "scriptsafe",
    #    "canvas-antifp",
       "adguard"
    #    "user-agent"
    ]

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
# metrics = ['usr (max)\n(in absolute)', 'usr (avg)\n(in absolute)', 'sys (max)\n(in absolute)', 'sys (avg)\n(in absolute)', 'load_time\n(in seconds)', 'data_usage\n(in MB)', 'RAM_usage_max\n(in MB)', 'RAM_usage_avg\n(in MB)', 'JSHeapSizeUsed\n(in MB)', '#frames\n(in absolute)', '#third_party\n(in absolute)']
# metrics = ['CPU Usage (avg)\n(in percentage)', 'CPU Usage (sys_avg)\n(in percentage)', 'Load time\n(in s)', 'Data Usage\n(in MB)', 'RAM Usage (avg)\n(in MB)']
metrics = ['CPU Usage (avg)\n(in percentage)', 'Data Usage\n(in MB)', 'RAM Usage (avg)\n(in MB)']
# metrics = ['load_time\n(in seconds)', 'data_usage\n(in MB)']

# Generate some random data for demonstration purposes
# np.random.seed(0)  # for reproducibility
# data = np.random.rand(num_metrics, num_extensions, 50)

content = json.load(open('../performance/data_usage/plot_content_selenium_1000.json', 'r'))
frames = json.load(open('../effective/ads/plot_frames.json', 'r'))
performance = json.load(open('../performance/cpu_load/plot/plot_performance.json', 'r'))
performance2 = json.load(open('../performance/cpu_load/plot/plot_performance2.json', 'r'))
third_party = json.load(open('../effective/third_party/plot_third_party.json', 'r'))
ram = json.load(open('../performance/cpu_load/plot/plot_ram.json', 'r'))
jsheap = json.load(open('../performance/cpu_load/plot/plot_jsheap.json', 'r'))

data = []

third_party_min = 999999
third_party_weights = {}

extn_except = ['decentraleyes', 'https', 'canvas-antifp', 'user-agent']

for extn in extensions:
    if extn not in extn_except:
        third_party_min = np.minimum(third_party_min, np.absolute(np.average(np.array(third_party[extn]))))

for extn in extensions:
    # third_party_cent[extn] = np.array(third_party[extn])/third_party_sum
    if extn not in extn_except:
        third_party_weights[extn] = np.absolute(np.average(np.array(third_party[extn])))/third_party_min
    else:
        third_party_weights[extn] = 1
print(third_party_weights)
# import sys
# sys.exit(0)

for extn in extensions:
    print(extn)
    print('cpu', round(np.mean(np.array(performance['cpu_avg'][extn])), 2), round(np.std(np.array(performance['cpu_avg'][extn])), 2))
    print('data', round(np.mean(np.array(content[extn])), 2), round(np.std(np.array(content[extn])), 2))
    print('ram', round(np.mean(np.array(ram['ram_avg'][extn])), 2), round(np.std(np.array(ram['ram_avg'][extn])), 2))
    print('-'*50)

    each_extn = []
    # each_extn.append(np.array(performance['usr_max'][extn]))
    # each_extn.append(np.array(performance['usr_avg'][extn]))
    each_extn.append(np.array(performance['cpu_avg'][extn]))
    # each_extn.append(np.array(performance['sys_max'][extn]))
    # each_extn.append(np.array(performance['sys_avg'][extn]))
    # each_extn.append(np.clip(np.array(performance2['load_time'][extn])/1000, -50, 50))
    # print(np.array(content[extn]))
    each_extn.append(np.array(content[extn]))
    # each_extn.append(np.array(ram['ram_max'][extn]))
    each_extn.append(np.array(ram['ram_avg'][extn]))
    # each_extn.append(np.array(jsheap['jsheap'][extn]))
    # each_extn.append(np.array(frames[extn]))
    # each_extn.append(np.array(third_party[extn]))
    data.append(each_extn)
# data = np.random.rand(8, 4, 20)  # now each metric has 2 values
data = np.array(data, dtype=object)

# # Create a new figure with three axes
# fig, axs = plt.subplots(3, 1, figsize=(10, 10))
fig = plt.figure(figsize=(10,15))

# Create a color map for the extensions
color_map = plt.cm.get_cmap('Set3', num_extensions)

# # y_limits
# y_limits = [(0, 100), (0, 0.5), ..., (lower_limit11, upper_limit11)]  # replace with the actual limits


# Create subplots for the first row
axs_1 = [plt.subplot(3, num_metrics_1, i+1) for i in range(num_metrics_1)]
# Create subplots for the second row
# axs_2 = [plt.subplot(3, num_metrics_1, num_metrics_1+i+1) for i in range(num_metrics_2)]
# Create subplots for the third row
# axs_3 = [plt.subplot(3, num_metrics_1, 2*num_metrics_1+i+1) for i in range(num_metrics_3)]

# Combine all axes in a list
axs = axs_1 #+ axs_2# + axs_3

# # For each metric in the first group...
# for i in range(num_metrics_1):
#     # For each extension...
#     min_ylimit = 10000 
#     max_ylimit = 0
#     for j in range(num_extensions):
#         # Create a boxplot for the extension's data for the current metric
#         boxplot = axs[0].boxplot(data[j, i], positions=[i*(num_extensions*box_width + gap) + j*box_width], widths=box_width, patch_artist=True, showfliers=False)
#         min_ylimit = min(min_ylimit, np.min(data[j, i]))
#         max_ylimit = max(max_ylimit, np.max(data[j, i]))
#         # Color the boxplot according to the extension number
#         for patch in boxplot['boxes']:
#             patch.set_facecolor(color_map(j))

#     # Set the y-axis limits for this metric
#     axs[0].set_ylim((min_ylimit, max_ylimit))

# # Set the x-tick labels to be the metric numbers
# axs[0].set_xticks([(num_extensions*box_width)/2 + i*(num_extensions*box_width + gap) for i in range(num_metrics_1)])
# axs[0].set_xticklabels([f'{metrics[i]}' for i in range(num_metrics_1)])

# # Repeat the process for the second group of metrics
# for i in range(num_metrics_1, num_metrics_1 + num_metrics_2):
#     min_ylimit = 10000 
#     max_ylimit = 0
#     for j in range(num_extensions):
#         boxplot = axs[1].boxplot(data[j, i], positions=[(i-num_metrics_1)*(num_extensions*box_width + gap) + j*box_width], widths=box_width, patch_artist=True, showfliers=False)
#         min_ylimit = min(min_ylimit, np.min(data[j, i]))
#         max_ylimit = max(max_ylimit, np.max(data[j, i]))

#         for patch in boxplot['boxes']:
#             patch.set_facecolor(color_map(j))

#     # Set the y-axis limits for this metric
#     axs[1].set_ylim((min_ylimit, max_ylimit))

# axs[1].set_xticks([(num_extensions*box_width)/2 + i*(num_extensions*box_width + gap) for i in range(num_metrics_2)])
# axs[1].set_xticklabels([f'{metrics[i]}' for i in range(num_metrics_1, num_metrics_1 + num_metrics_2)])

# # Repeat the process for the third group of metrics
# for i in range(num_metrics_1 + num_metrics_2, num_metrics):
#     min_ylimit = 10000 
#     max_ylimit = 0
#     for j in range(num_extensions):
#         boxplot = axs[2].boxplot(data[j, i], positions=[(i-num_metrics_1-num_metrics_2)*(num_extensions*box_width + gap) + j*box_width], widths=box_width, patch_artist=True, showfliers=False)
#         min_ylimit = min(min_ylimit, np.min(data[j, i]))
#         max_ylimit = max(max_ylimit, np.max(data[j, i]))
        
#         for patch in boxplot['boxes']:
#             patch.set_facecolor(color_map(j))
#     # Set the y-axis limits for this metric
#     axs[2].set_ylim((min_ylimit, max_ylimit))

# For each metric
for i in range(num_metrics):
    # For each extension
    min_ylimit = 10000 
    max_ylimit = 0
    for j in range(num_extensions):
        # Create a boxplot for the extension's data for the current metric
        boxplot = axs[i].boxplot(data[j, i], positions=[j*(box_width+gap_within_metric)], widths=box_width, patch_artist=True, showfliers=False)
        
        # lower_whisker = boxplot['whiskers'][0].get_ydata()[1]
        # upper_whisker = boxplot['whiskers'][1].get_ydata()[1]
        # diff = (upper_whisker - lower_whisker)/5
        # min_ylimit = min(min_ylimit, lower_whisker)
        # max_ylimit = max(max_ylimit, upper_whisker)
        
        # Color the boxplot according to the extension number
        for patch in boxplot['boxes']:
            patch.set_facecolor(color_map(j))
            patch.set_linewidth(0.5)  # Set whisker line width
            # patch.set_edgecolor('lightgray')  # Set edgecolor to light gray
        for whisker in boxplot['whiskers']:
            # whisker.set_color('lightgray')  # Set whisker color to light gray
            whisker.set_linewidth(0.5)  # Set whisker line width
        for cap in boxplot['caps']:
            # cap.set_color('lightgray')  # Set cap color to light gray
            cap.set_linewidth(0.5)  # Set cap line width



    # axs[i].set_ylim((min_ylimit-diff, max_ylimit+diff))  # Set the y-axis limits for this metric
    axs[i].set_xticks([])  # Remove x-ticks
    axs[i].set_xlabel(f'{metrics[i]}', fontsize=15)  # Set x-label to metric number
    # axs[i].set_yscale('symlog')
# axs[2].set_xticks([(num_extensions*box_width)/2 + i*(num_extensions*box_width + gap) for i in range(num_metrics - num_metrics_1 - num_metrics_2)])
# axs[2].set_xticklabels([f'{metrics[i]}' for i in range(num_metrics_1 + num_metrics_2, num_metrics)])

# Create a custom legend
legend_elements = [plt.Line2D([0], [0], color=color_map(i), lw=4, label=f'{extn_dict[extensions[i]]}') for i in range(num_extensions)]
# fig.legend(handles=legend_elements, prop={'size': 6}, loc='lower right', bbox_to_anchor=(0.96, 0.05), ncols=2)
fig.legend(handles=legend_elements, prop={'size': 10}, loc='lower right',bbox_to_anchor=(0.90, 0.58), ncols=7)

# # Create a custom legend
# legend_elements = [plt.Line2D([0], [0], color=color_map(i), lw=4, label=f'{extensions[i]}') for i in range(num_extensions)]
# # Place the legend in the third subplot (third row) at the top
# axs[2].legend(handles=legend_elements, loc='upper right')

# Add vertical lines with text
# fig.text(0.98, 0.7, '-------------- Performance --------------', rotation=270, weight='bold', style='italic', verticalalignment='center')
# fig.text(0.98, 0.2, '----- Effectiveness -----', rotation=270, weight='bold', style='italic', verticalalignment='center')

# plt.tight_layout()
plt.show()
# plt.savefig('boxplot.pdf', bbox_inches='tight')