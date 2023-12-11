import re

def count_filters(file_path):
    url_filter_count = 0
    html_filter_count = 0
    exception_rule_count = 0
    comment_count = 0
    blank_line_count = 0

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                blank_line_count += 1
                continue
            if line.startswith('!'):
                comment_count += 1
                continue
            if line.startswith('@@'):
                exception_rule_count += 1
            elif '##' in line or '#@#' in line:
                html_filter_count += 1
            else:
                url_filter_count += 1

    return url_filter_count, html_filter_count, exception_rule_count, comment_count, blank_line_count

import os
path = f"./filterlist/adguard/"
dir_list = os.listdir(path)

url_count = 0
html_count = 0
exception_count = 0
comment_count = 0
blank_count = 0
for f in dir_list:
    file_path = path+f
    url_count1, html_count1, exception_count1, comment_count1, blank_count1 = count_filters(file_path)
    url_count += url_count1 
    html_count += html_count1 
    exception_count += exception_count1 
    comment_count += comment_count1 
    blank_count += blank_count1 

print(f"URL Filters: {url_count}, HTML Filters: {html_count}, Exception Rules: {exception_count}, Comments: {comment_count}, Blank Lines: {blank_count}")
