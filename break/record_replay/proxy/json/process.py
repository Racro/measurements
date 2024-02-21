import json

extn_lst = {"ublock", "adblock", "privacy-badger"}
ublock_urls = ["ublockorigin.pages.dev", 'cdn.statically.io', 'publicsuffix.org', 'malware-filter.gitlab.io', ]

for extn in extn_lst:
    f = json.load(open(f'{extn}missing.json' ,'r'))
    sites = list(f.keys())

    compare_dict = {}
    for site in sites:
        missing = f[site]['missing_resources']
        additional = f[site]['additional_resources']

        miss_sets = []
        addn_sets = []

        for url in additional:
            if url[-1] == True or url[1] == 204 or url[-3] == '' or url[0].split('/')[2] in ublock_urls:
                continue
            
            url_domain = ''.join(url[0].split('/')[2])
            addn_sets.append((url_domain, url[-3].split(";")[0], url[0]))
            
        for url in missing:
            if url[-1] == True or url[1] == 204 or url[-3] == '':
                continue
            
            url_domain = ''.join(url[0].split('/')[2])
            miss_sets.append((url_domain, url[-3].split(";")[0], url[0]))
            
        miss_sets = set(miss_sets)
        addn_sets = set(addn_sets)

        compare_dict[site] = {}
        compare_dict[site]["missing"] = list(miss_sets - addn_sets)
        compare_dict[site]["additional"] = list(addn_sets - miss_sets)

    json.dump(compare_dict, open(f'{extn}_diff.json', 'w'))

