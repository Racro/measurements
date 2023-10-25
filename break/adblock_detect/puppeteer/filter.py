benign = ["yahoo","geocities","fandom","wikia","opera","time","zillow","zdnet","softonic","gamespot","gogriz","eventbrite","intel","entrepreneur","techtarget","flaticon","theporndude","history","thingiverse","crunchbase","realtor","brave","teads","moneycontrol","onmsft","careerindia","dreamstime","traveler","cdiabetes","tacorelish","massagewarehouse","viavisolutions"]

import json

data = json.load(open('adblock_detect_custom.json', 'r'))

extn_lst = list(data.keys())
new_data = {}

for extn in data:
    if extn != 'control':
        new_data[extn] = []
        for i in range(len(data[extn])):
            check = 0
            for j in benign:
                if j in data[extn][i][0]:
                    check = 1
                    break
            if check:
                continue
            else:
                new_data[extn].append(data[extn][i][0])

print(new_data['https'])
for extn in new_data:
    print(extn, len(new_data[extn]))
                
            