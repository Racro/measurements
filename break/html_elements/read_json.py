import json

a = json.load(open('json/sample_sites.json', 'r'))
b = json.load(open('json/links_control.json', 'r'))
c = json.load(open('json/drop downs_control.json', 'r'))
d = json.load(open('json/login_control.json', 'r'))

a = list(a.keys())
b = list(b.keys())
c = list(c.keys())
d = list(d.keys())

print(len(a), len(b), len(c) ,len(d))

all_sites_data = set(a) | set(b) | set(c) | set(d)
all_sites = json.load(open('websites.json', 'r'))

diff = set(all_sites) - all_sites_data
# print(diff)
# import OS module
import os
# Get the list of all files and directories
path = "./page_ss"
dir_list = os.listdir(path)
# print("Files and directories in '", path, "' :")
# prints all files
# print(dir_list)

# for i in diff:


# print(diff)