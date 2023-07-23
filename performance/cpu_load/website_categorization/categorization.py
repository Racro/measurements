import json

extensions_configurations = [
       # No extensions
    #    "",
    #    # Extensions on their own
       "adblock",
       "decentraleyes",
       "disconnect",
       "ghostery",
       "https",
       "noscript",
       "privacy-badger",
       "ublock",
       "scriptsafe",
       "canvas-antifp",
       "adguard",
       "user-agent"
       # Combinations
    #    "decentraleyes,privacy_badger,ublock_origin"
    ]

f1 = open('site_load_time_custom2_1000.json', 'r')
# f2 = open('website_categories.json', 'r')
# f3 = open('website_categories_less.json', 'r')

# categories = json.load(f2)
# dummy_dict = json.load(f3)
 
# categories_new = {}
# dummy_dict_new = {}

# for key in categories:
#     categories_new[key] = []
#     for site in categories[key]:
#         lst = site.split(".")
#         if len(lst) > 2:
#             if lst[0] not in categories_new[key]:
#                 categories_new[key].append(lst[0])
#             if lst[1] not in categories_new[key]:
#                 categories_new[key].append(lst[1])
#         else:
#             if lst[0] not in categories_new[key]:
#                 categories_new[key].append(lst[0])

# for key in dummy_dict:
#     dummy_dict_new[key] = []
#     for site in dummy_dict[key]:
#         lst = site.split(".")
#         if len(lst) > 2:
#             if lst[0] not in dummy_dict_new[key]:
#                 dummy_dict_new[key].append(lst[0])
#             if lst[1] not in dummy_dict_new[key]:
#                 dummy_dict_new[key].append(lst[1])
#         else:
#             if lst[0] not in dummy_dict_new[key]:
#                 dummy_dict_new[key].append(lst[0])
        
# for key in dummy_dict_new:
#     if key not in categories_new.keys():
#         categories_new[key] = dummy_dict_new[key]
#     else:
#         for root in dummy_dict_new[key]:
#             if root not in categories_new[key]:
#                 categories_new[key].append(root)

sites = json.load(f1)

f4 = open('website_roots.json', 'r')
categories_new = json.load(f4)
f4.close()                

table_min = [] # for printing
table_max = [] # for printing
for extn in extensions_configurations:
    n = 1
    for site in list(sites[extn].keys())[1:101]:
        lst = site.split(".")
        if len(lst) > 2:
            root = lst[1]
        else:
            root = lst[0]
        check = 0 
        
        if sites[extn][site] > -5000:
            continue

        # print(root)
        for key in categories_new:
            for val in range(len(categories_new[key])):
                if root in categories_new[key][val]:
                    check = 1
                    table_min.append([extn, n, sites[extn][site], site, key])
                    break
            if check==1:
                break
        if check == 0:
            table_min.append([extn, n, sites[extn][site], site, 'NULL'])
        n += 1

    for site in list(sites[extn].keys())[-100:]:
        lst = site.split(".")
        if len(lst) > 2:
            root = lst[1]
        else:
            root = lst[0]
        check = 0 
        
        if sites[extn][site] < 5000:
            continue

        # print(root)
        for key in categories_new:
            for val in range(len(categories_new[key])):
                if root in categories_new[key][val]:
                    check = 1
                    table_max.append([extn, n, sites[extn][site], site, key])
                    break
            if check==1:
                break
        if check == 0:
            table_max.append([extn, n, sites[extn][site], site, 'NULL'])
        n += 1

# from tabulate import tabulate
# print(tabulate(table_min))
# print(tabulate(table_max))
#print(n)
import csv
f = open('analysis1.csv', 'w')

csvwriter = csv.writer(f)

# writing the fields 
csvwriter.writerow(['Extension', 'index', 'load_time', 'website', 'key']) 
    
# writing the data rows 
csvwriter.writerows(table_min)
csvwriter.writerow(['','','','',''])
csvwriter.writerows(table_max)
f.close()

f1.close()
