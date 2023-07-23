import random
import json
# Your original dictionary with 44 keys and lists of strings as values
original_dict = json.load(open('categories.json', 'r'))

# New dictionary to store the results
new_dict = {}

# Iterate through the original dictionary
for key, value_list in original_dict.items():
    # If the value list has 25 or more elements, sample 25 random strings
    if len(value_list) >= 25:
        new_dict[key] = random.sample(value_list, 25)
    else:
        # If the value list has less than 25 elements, include the entire list
        new_dict[key] = value_list

json.dump(new_dict, open('website_pool.json', 'w'))
# Now, new_dict contains the 44 keys with either 25 random strings or the entire list
