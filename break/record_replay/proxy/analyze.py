import subprocess
import json
content_type = ['javascript', 'image', 'video', 'html']

avg_data = {}

for content in content_type:
    avg_data[content] = []
    try:
        result = subprocess.run(['python3', 'process.py', content], stdout=subprocess.PIPE)
        f = open(f'analyse_{content}.json', 'r')
        data_dict = json.load(f)
        f.close()
        for key in data_dict:
            value = []
            for site in data_dict[key]:
                lst = list(data_dict[key][site].values())
                if (max(lst) == min(lst)):
                    continue
                value.append(max(lst) - min(lst))
                # print(value)
            if len(value) > 0:
                avg_data[content].append(round(sum(value)/len(value), 2))

    except Exception as e:
        print(e, content)
        continue 

f = open('avg_range_data.json', 'w')
json.dump(avg_data, f)
f.close()