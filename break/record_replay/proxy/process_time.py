import json

extn_lst = ['adblock', 'ublock', 'privacy-badger']

def avg(list_of_lists):
    sums = []
    for list_ in list_of_lists:
        sum_first_index = sum(sublist[0] for sublist in list_)/len(list_)
        sum_second_index = sum(sublist[1] for sublist in list_)/len(list_)
        sums.append((sum_first_index, sum_second_index))
    return [sums[0][1], sums[1][1], sums[2][1]]

def last_index(list_of_lists):
    sums = []
    for list_ in list_of_lists:
        sum_first_index = list[-1]
        sum_second_index = list[-1]
        sums.append((sum_first_index, sum_second_index))
    return [sums[0][1], sums[1][1], sums[2][1]]

error = {}
data1 = {}
data2 = {}
for extn in extn_lst:
    data1[extn] = [[], [], []]
    data2[extn] = [[], [], []]
    error[extn] = 0
    extn_data = json.load(open(f'json_time/{extn}.json', 'r'))
    websites = list(extn_data.keys())

    for website in websites:
        pre = extn_data[website][0]
        during = extn_data[website][1]
        post = extn_data[website][2]

        pre.remove([])
        during.remove([])
        post.remove([])
        pre.remove([-1, -1])
        during.remove([-1, -1])
        post.remove([-1, -1])

        if len(pre) < 2 or len(post) < 2 or len(during) < 2:
            if len(during) == 0:
                error[extn] += 1 
            continue
        
        pre = pre[1:] # to account for cache change
        during = during[1:] # to account for cache change
        prost = post[1:] # to account for cache change

        ret = avg([pre, during, post])
        ret2 = last_index([pre, during, post])

        for i in range(3):
            data1[extn][i].append(ret[i])
            data2[extn][i].append(ret2[1])

dump_dict = {}
dump_dict['avg'] = data1
dump_dict['last'] = data2
dump_dict['error'] = error

json.dump(dump_dict, open("data_time.json", "w"))

#####

import matplotlib.pyplot as plt

# Example data for 3 extensions, each with 3 lists of data
ext1_data = dump_dict['avg']['ublock']
ext2_data = dump_dict['avg']['adblock']
ext3_data = dump_dict['avg']['privacy-badger']

# Combine all data into a list for easier iteration
all_data = ext1_data + ext2_data + ext3_data

# Positions for each group of boxplots
positions = [1, 2, 3, 5, 6, 7, 9, 10, 11]

# Creating the boxplot
plt.figure(figsize=(10, 6))
plt.boxplot(all_data, positions=positions)

# Customizing the plot
plt.title('Boxplot Clusters for Each Extension')
plt.xlabel('Extension Group')
plt.ylabel('Value')

# Adding custom x-ticks to denote different clusters
tick_positions = [2, 6, 10]  # Midpoint of each cluster for labeling
plt.xticks(tick_positions, ['ublock', 'adblock', 'privacy-badger'])

# Adding grid for better readability
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Show the plot
plt.show()


        