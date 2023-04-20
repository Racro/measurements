from bs4 import BeautifulSoup
import random 
import requests
import time
# updated_list = []

# sites = ["geeksforgeeks.org", "forbes.com", "insider.com"]

def find_inner_pages(sites, updated_dict = {}):
    href_count = {}
    for site in sites:
        try:
            response = requests.get("http://www." + site, timeout=5)
        except requests.exceptions.Timeout as e:
            print("Site timed out: ", site)
        except requests.exceptions.ConnectionError as e:
            print(f"Connection error for {site}... Trying without www option")
            try:
                response = requests.get("http://" + site, timeout=5)
            except Exception as e:
                print("without www fail: ", site)
                continue
        except Exception as e:
            print("Not reachable: ", site)
            continue

        time.sleep(2)
        updated_dict[site] = ["http://" + site]
        soup = BeautifulSoup(response.content, 'html.parser')
        href_links = []
        for link in soup.find_all('a'):
            try:
                if len(link.contents) >= 1:
                    site_str = "." + site
                    if link.get('href'):
                        if link.get("href")[0] == '/':
                            href_links.append("http://" + site + link.get("href"))
                        elif site_str in link.get("href"):
                            href_links.append(link.get("href"))
            except Exception as e:
                print(e)

        href_count[site] = len(href_links)
    
    # import json
    # f = open("href_count.json", "w")
    # json.dump(href_count, f)
    # f.close()

        if len(href_links) > 10:
            random.shuffle(href_links)
            updated_dict[site].extend(href_links[:2])
    
    return updated_dict
    
# from tranco import Tranco
# t = Tranco(cache=True, cache_dir='.tranco')
# latest_list = t.list()
# latest_list = latest_list.top(1000)
# find_inner_pages(latest_list)