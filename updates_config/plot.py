# Let's import the necessary libraries and read the data first
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as mdates
import numpy as np
import pickle

import matplotlib
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

df = pd.read_csv('./review_sentiment.csv')
df2 = pd.read_csv('./release.csv')

f = open('../../review_extraction/pickle_files/sentimentscore_vs_time_new.pickle', 'rb')
review_set = pickle.load(f)

df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df.sort_values('Timestamp', inplace=True)

df2['Timestamp'] = pd.to_datetime(df2['Timestamp'])

extn_lst = ['adblock-plus-free-ad-bloc', 'ublock-origin', 'ghostery-–-privacy-ad-blo', 'privacy-badger', 'adguard-adblocker']
extn_dict = {'adblock-plus-free-ad-bloc': 'ABP', 'ublock-origin': 'UbO', 'ghostery-–-privacy-ad-blo': 'Ghostery', 'privacy-badger': 'PB', 'adguard-adblocker': 'AdG'}
#extn_lst = ['ABP', 'UbO', 'Ghostery', 'PB', 'AdG']
# Define the number of plots and their arrangement
# n = len(df['Extension'].unique())
n = n_filtered = 5
ncols = 1
nrows = nrows_filtered = n // ncols if n % ncols == 0 else n // ncols + 1

# Define a color list for better differentiation
color_list = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan']

fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(15, 4*nrows))
color_list1 = color_list[:5]
color_list2 = color_list[5:]

lst = []
df_filtered = df
# filtering out extn other than 5
for extn in df['Extension'].unique():
    if extn not in extn_lst:
        df_filtered = df_filtered[df_filtered['Extension'] != extn]

# filtering out sentiment scores -0.7 < s < 0.7
df_filtered = df_filtered[df_filtered['Score'].abs() >= 0.7]
# print(df_filtered.head())

fig, axes = plt.subplots(nrows=nrows_filtered, ncols=ncols, figsize=(10, 4*nrows_filtered))

# Flatten the axes array and remove excess plots
axes = axes.flatten()
if len(axes) > n_filtered:
    for ax in axes[n_filtered:]:
        fig.delaxes(ax)

start_date = datetime.date(2012, 1, 1)
end_date = datetime.date(2023, 1, 1)

for i, extension in enumerate(df_filtered['Extension'].unique()):
    df_extension = df_filtered[df_filtered['Extension'] == extension]
    rolling_avg = df_extension['Score'].rolling(window=60).mean()
    axes[i].plot(df_extension['Timestamp'], rolling_avg, label=extension, color=color_list1[i % len(color_list1)])
    axes[i].set_title(extn_dict[extension], fontsize=16, pad=-10)
    # axes[i].set_xlabel('Date')
    axes[i].set_ylim([-1, 1])  # Set y-axis limit
    axes[i].set_xlim([start_date, end_date])  # Set y-axis limit
    axes[i].grid(True)
    axes[i].tick_params(axis='y', labelsize=16)

    # axes[i].tick_params(axis='x', rotation=45)
    # print(extension)
    if extension == 'adguard-adblocker':
        axes[i].set_ylabel('Criticality Score', fontsize=20)
    if extension == 'privacy-badger':
        axes[i].tick_params(axis='x', rotation=45, labelsize=16)
        axes[i].set_xlabel('Date', fontsize=16)
    else:
        axes[i].tick_params(labelbottom = False)

review_num = {}
mask_pos = {}
mask_neg = {}

for extn in review_set:
    # review_set[extn] = np.array(review_set[extn], dtype=object)
    if extn in extn_lst:
        review_num[extn] = [[], []]
        for i in range(len(review_set[extn][1])):
            review_set[extn][0][i][0] = np.array(review_set[extn][0][i][0])
            review_num[extn][0].append(len(review_set[extn][0][i][0][review_set[extn][0][i][0] <= -0.7]))
            review_num[extn][1].append(review_set[extn][1][i])
        review_num[extn][0] = np.array(review_num[extn][0][:-1])
        review_num[extn][1] = np.array(review_num[extn][1][:-1])
        # mask_pos[extn] = review_num[extn][0] >= 0.7
        # mask_neg[extn] = review_num[extn][0] <= -0.7

axes2 = []
for i in axes:
    axes2.append(i.twinx())
axes2 = np.array(axes2, dtype=object)

for i, extension in enumerate(df_filtered['Extension'].unique()):
    # df_extension = df2[df2['Extension'] == extension]
    # rolling_avg = df_extension['Score'].rolling(window=60).mean()
    # if extension == 'ghostery-–-privacy-ad-blo':
    #     print(rolling_avg)
    axes2[i].plot(review_num[extension][1], review_num[extension][0], label=extn_dict[extension], color=color_list2[i % len(color_list2)])
    #axes2[i].set_title(extn_dict[extension])
    # axes2[i].set_xlabel('Date')
    if extension == 'adguard-adblocker':
        axes2[i].set_ylabel('#Critical_Reviews', fontsize=20)
    axes2[i].set_ylim([0, max(review_num[extension][0])+100])  # Set y-axis limit
    axes2[i].set_xlim([start_date, end_date])  # Set y-axis limit
    axes2[i].grid(True)
    axes2[i].tick_params(axis='y', labelsize=16)
    # axes2[i].tick_params(axis='x', rotation=45)

for ax in axes:
    ax.xaxis.set_minor_locator(mdates.DayLocator(interval=90))
    ax.grid(True, which='minor', axis='x', linestyle='--')
    
    # X-ticks every 2 years
    ax.xaxis.set_major_locator(mdates.YearLocator(2))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

# plt.xticks(fontsize=15)
# plt.yticks(fontsize=15)
# plt.legend(fontsize='14', loc='upper left', bbox_to_anchor=(0.05, 1.0))
fig.suptitle('Review Sentiment Over Time for Each Extension (60-day Rolling Average)', fontsize=16)
fig.tight_layout()
plt.show()
