import os
import json
import sys

path1 = f"./data_custom/"
path2 = f"./../docker/chrome/data/"
dir_list1 = os.listdir(path1)
dir_list2 = os.listdir(path2)

for website in dir_list2:
    print(website)
    f = open(path2+website, 'r')
    ua_data = json.loads(f.read())
    f.close()

    try:
        f = open(path1+website, 'r')
        parent_data = json.loads(f.read())
        f.close()
    except Exception as e:
        print(e)
        continue

    try:
        parent_data['stats']['user-agent'] = ua_data['stats']['user-agent']
    except Exception as e:
        print(e)
        continue
    
    f = open(path1+website, 'w')
    json.dump(parent_data, f)
    f.close()