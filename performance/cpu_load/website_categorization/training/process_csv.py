import csv 

category_dict = {}

with open('training_data_en.csv') as f:
    csv_reader = csv.reader(f, delimiter=',')
    for row in csv_reader:
        category = row[3].split('/')[1]
        if category in category_dict.keys():
            category_dict[category].append(row[2])
        else:
            category_dict[category] = []
f.close()
    
import json
with open("website_categories.json", "w") as f:
    json.dump(category_dict, f)
f.close()
