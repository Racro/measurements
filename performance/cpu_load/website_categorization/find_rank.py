import json
from tranco import Tranco 

d = json.load(open('categories.json', 'r')) 

for key in d.keys(): 
    for index in range(len(d[key])): 
        lst = d[key][index].split('.') 
        if lst[0] == 'www': 
            lst = lst[1:] 
        if len(lst) > 2: 
            if len(lst[-2]) > 4: 
                lst = lst[1:] 
        d[key][index] = '.'.join(lst)
    d[key] = list(set(d[key]))

t = Tranco(cache=True, cache_dir='.tranco') 
latest_list = t.list()

rank = {}
for key in d.keys():
    rank[key] = [] 
    for site in d[key]: 
        rk = latest_list.rank(site) 
        if rk == -1:
            continue
        rank[key].append(rk)

json.dump(rank, open('rank.json', 'w'))