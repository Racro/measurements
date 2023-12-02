# filter out websites at rank 1..1000, 1500, 2000, 2500, 3000, ......
# to cover both popular and unpopular websites

# from tranco import Tranco
# t = Tranco(cache=True, cache_dir='.tranco')
# latest_list = t.list()
# total_list = latest_list.top(300000)

total_list = []

import csv
with open('tranco_custom.csv') as f:
    csv_reader = csv.reader(f, delimiter=',')
    for row in csv_reader:
        total_list.append(row[1])

sites = total_list[:10000]
sites.extend(total_list[-10000:])

# index = 1000
# for i in range(500):
#     sites.append(total_list[index])
#     index = index + 500

# with open("test_sites_custom.txt", "w") as f:
with open("test_sites_custom_break.txt", "w") as f:
    for site in sites:
        f.write(site)
        f.write('\n')
f.close()
