import json

f1 = open('site_load_time_1000.json', 'r')
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
n = 1

f4 = open('website_roots.json', 'r')
categories_new = json.load(f4)
f4.close()                

table = [] # for printing
for site in list(sites['ub'].keys())[1:101]:
    lst = site.split(".")
    if len(lst) > 2:
        root = lst[1]
    else:
        root = lst[0]
    
    check = 0 
    
    # print(root)
    for key in categories_new:
        if root in categories_new[key]:
            check = 1
            table.append([n, sites['ub'][site], site, key])
            break
    if check == 0:
        table.append([n, sites['ub'][site], site, 'NULL'])
    n += 1    

from tabulate import tabulate
print(tabulate(table))
#print(n)

f1.close()
# f2.close()
# f3.close()

    
