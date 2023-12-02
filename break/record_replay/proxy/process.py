import json
import argparse
import os
# parser = argparse.ArgumentParser()
# parser.add_argument('website')
# args = parser.parse_args()
from filterrule import *
import sys

path = f"./ublock/"
dir_list = os.listdir(path)

parser = argparse.ArgumentParser(prog='process', usage='python3 process.py [website] [content]')
# parser.add_argument('website', type=str)
parser.add_argument('content', type=str, default='javascript')
args = parser.parse_args()
patterns = get_patterns()
seen_patterns = []
whitelist = []
analze = {}

for website in dir_list:
    # if (website == args.website):
        # data_dict = json.load(open(path+website, 'r'))[f'./{website}']
    data_dict = json.load(open(path+website, 'r'))

    prev = {}
    after = {}

    tup1 = []
    tup2 = {}

    # prev['url'] = []
    # prev['method'] = []
    # prev['queryString'] = []
    # prev['headersSize'] = []
    # prev['status'] = []

    after['url'] = {}
    after['method'] = {}
    after['queryString'] = {}
    after['headersSize'] = {}
    after['status'] = {}
    after['data'] = {}
    after['data2'] = {}
    after['serverIP'] = {}
    after['cookies'] = {}
    after['contentType'] = {}

    false = 0
    true = 0

    try:
        for i in data_dict.keys():
            # after[i] = []
            tup2[i] = []
            after['status'][i] = []
            after['data'][i] = 0
            after['data2'][i] = 0
            after['serverIP'][i] = []
            after['cookies'][i] = []
            after['contentType'][i] = []
            for j in range(len(data_dict[i])):
                url_lst = data_dict[i][j]['request']['url'].split('/')
                # after['url'][i].append(d[i][j]['request']['url'])
                # after['method'][i].append(d[i][j]['request']['method'])
                # after['queryString'][i].append(d[i][j]['request']['queryString'])
                # after['headersSize'][i].append(d[i][j]['request']['headersSize'])
                # after['serverIP'][i].append(data_dict[i][j]['serverIPAddress'])
                after['status'][i].append(data_dict[i][j]['response']['status'])
                after['contentType'][i].append(data_dict[i][j]['response']['content']['mimeType'])
                after['cookies'][i].append(data_dict[i][j]['response']['cookies'])
                # tup2.append((d[i][j]['request']['url'], d[i][j]['response']['status']))
                if (data_dict[i][j]['response']['status'] == 200 or data_dict[i][j]['response']['status'] == 204) and (args.content in data_dict[i][j]['response']['content']['mimeType']):
                    after['data'][i] += data_dict[i][j]['response']['bodySize']
                    after['data2'][i] += data_dict[i][j]['response']['content']['size']
                    tup2[i].append('/'.join(url_lst[0:3]))
                    # if len(url_lst) >= 4:
                    #     # tup2[i].append(('/'.join(url_lst[0:3]), d[i][j]['response']['status'], d[i][j]['serverIPAddress']))
                    #     tup2[i].append(('/'.join(url_lst[0:3]), d[i][j]['response']['status']))
                        
                    # else:
                    #     # tup2[i].append(('/'.join(url_lst[0:]), d[i][j]['response']['status'], d[i][j]['serverIPAddress']))
                    #     tup2[i].append(('/'.join(url_lst[0:]), d[i][j]['response']['status']))

                    # try:
                    #     res_bool = d[i][j]['request']['url'] == prev['request']['url']
                    #     if res_bool == False:
                    #         false += 1
                    #         print('prev: ', prev['request']['url'])
                    #         print('curr: ', d[i][j]['request']['url'])
                    #     else:
                    #         true += 1
                    # except Exception as e:
                    #     print(e)

        # print(set(after['status']['0']))
        # print(set(after['serverIP']['0']))
        # print(after['data'])
        # print(after['cookies']['2'])

        # ind = '2'
        # b = set(tup2[ind])
        # for i in list(b):
        #     print(i[0], i[2])
        # print('-'*50)
        # for i in tup2.keys():
        #     if i != ind:
        #         a = set(tup2[i])
        #         print(len(a & b), len(a), len(b))    

        #         for i in list(a-b):
        #             print(i[0], i[1], i[2])
        #             # print(i[0], i[1])
        #         print('-'*50)

        a = set(tup2['0'])
        b = set(tup2['1'])
        c = set(tup2['2'])
        d = set(tup2['3'])
        e = set(tup2['4'])
    except Exception as e:
        print(e)
        print(tup2.keys())
        print('-'*50)
        continue

    # print(len(tup2['0']))
    # print(len(a))
    # print(len(a & b ))
    # print(len(a & b & c))
    # print(len(a & b & c & d & e))

    intersect = list(a & b & c & d & e)

    data = {}
    data2 = {}
    analze[website] = {}

    for i in data_dict.keys():
        data[i] = 0
        data2[i] = 0
        for j in range(len(data_dict[i])):
            url = '/'.join(data_dict[i][j]['request']['url'].split('/')[0:3])
            # url2 = '/'.join(data_dict[i][j]['request']['url'].split('/')[0:3])
            url2 = data_dict[i][j]['request']['url']

            if (url in intersect) and (data_dict[i][j]['response']['status'] == 200 or data_dict[i][j]['response']['status'] == 204) and (args.content in data_dict[i][j]['response']['content']['mimeType']):
                # caching
                val = False
                if url not in whitelist:
                    val, pattern = check(url2, patterns, seen_patterns)
                    
                    if (val) and (pattern not in seen_patterns):
                        seen_patterns.append(pattern)
                    # print(val, pattern, url)
                    if (not val):
                        whitelist.append(url)

                if (not val):
                    # print(url, data_dict[i][j]['response']['bodySize'])
                    data[i] += data_dict[i][j]['response']['bodySize']
                    data2[i] += data_dict[i][j]['response']['content']['size']
                    if url2 not in analze[website].keys():
                        # if url == 'https://ads-us.pictela.net':
                        analze[website][url2] = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0}
                    analze[website][url2][i] = data_dict[i][j]['response']['content']['size']
                        # if data_dict[i][j]['response']['bodySize'] == 0:
                        #     print(url)
                    # else:
                    #     analze[website][url2][i] += data_dict[i][j]['response']['content']['size']

f = open(f'analyse_{args.content}.json', 'w')
json.dump(analze, f)
f.close()
    # for key in analze:
    #     # if 0 in analze[key].values():
    #     if len(set(analze[key].values())) > 1:
    #         print(key, analze[key].values()) 
    # # print(analze)
    # print(website)
    # print(whitelist)
    # print('all_urls_truncated', len(tup2['1']))
    # print('url_truncated_set:', len(b))
    # print('url_truncated_intersected_set:', len(a & b & c & d & e))
    # print('url_intersected_set', len(analze.keys()))
    # # print(a & b & c & d & e)
    # print(after['data'])
    # print(after['data2'])
    # print(data)
    # print(data2)
    # diff_dict = {}
    # diff_dict2 = {}
    # for key in after['data']:
    #     diff_dict[key] = after['data'][key] - data[key]
    #     diff_dict2[key] = after['data2'][key] - data2[key]
    # print(diff_dict)
    # print(diff_dict2)
    # # print(set(after['contentType']["0"]))

    # print('-'*50)
    # break
    # # print(len(tup2['0'] & tup2['1'] & tup2['2'] & tup2['3'] & tup2['4']))
    # # print(len(a & b & c & d & e))

# print('true:', true)
# print('false:', false)
# print(prev['status'])
# print(after['status'])

# print(len(tup1))
# a = set(tup1)
# b = set(tup2)
# # print(len(a), len(b))
# print(len(a & b), len(a), len(b))
# # print(a & b)

# # print(len(prev['url']))
# # print(len(after['url']))
# # a = set(prev['url'])
# # b = set(after['url'])
# # print(len(a & b), len(a))

# for i in list(a-b):
#     print(i[0], i[1])
# print('-'*50)
# for i in list(b-a):
#     print(i[0], i[1])


# {0, 200, 204, 301, 302, 303, 400, 206, 307, 403, 404} - pre ublock
# {200, 400, 206} - post ublock
# dict_keys(['pageref', 'startedDateTime', 'request', 'response', 'cache', 'timings', 'serverIPAddress', 'comment', 'time'])
# >>> d["0"][0]['request'].keys()
# dict_keys(['method', 'url', 'httpVersion', 'cookies', 'headers', 'queryString', 'headersSize', 'bodySize', 'comment'])
# >>> d["0"][0]['response'].keys()
# dict_keys(['status', 'statusText', 'httpVersion', 'cookies', 'headers', 'content', 'redirectURL', 'headersSize', 'bodySize', 'comment'])
# {'0': 17726591, '1': 17105062, '2': 23334712, '3': 38751312, '4': 17287086} - diff in data
# {url, serverIP} is different
# cookies is empty for both request and response
 
# {'', 'application/javascript; charset=utf-8', 'application/octet-stream', 'text/javascript; charset=UTF-8', 'text/html; charset=utf-8', 'application/json; charset=utf-8', 'application/javascript', 'application/x-javascript', 'text/html; charset=UTF-8', 'video/mp4', 'text/plain; charset=utf8', 'image/vnd.microsoft.icon', 'text/css', 'text/vtt', 'image/svg+xml', 'binary/octet-stream', 'text/javascript; charset=utf-8', 'font/woff2', 'application/json;charset=utf-8', 'application/json; charset=UTF-8', 'image/jpeg', 'application/x-protobuf', 'application/json', 'application/xml', 'image/webp', 'text/plain; charset=UTF-8', 'image/png', 'text/html', 'text/plain', 'text/vtt; charset=UTF-8', 'text/plain; charset=utf-8', 'image/gif', 'text/html;charset=UTF-8', 'text/javascript'}

