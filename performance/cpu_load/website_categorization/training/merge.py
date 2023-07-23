import json

d1 = json.load(open('website_categories.json', 'r'))
d2 = json.load(open('website_categories_less.json', 'r')) 

cat1 = list(d1.keys())
cat2 = list(d2.keys())

for i in range(len(cat2)):
    old = cat2[i]
    cat2[i] = cat2[i].replace('-', ' ')
    cat2[i] = cat2[i].replace('and', '&')
    if cat2[i] not in list(d2.keys()):
        d2[cat2[i]] = d2[old]
        del d2[old]

for cat in cat2:
    for site in d2[cat]:
        if site not in d1[cat]:
            d1[cat].append(site)

json.dump(d1, open('../categories.json', 'w'))