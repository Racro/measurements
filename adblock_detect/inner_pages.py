from bs4 import BeautifulSoup
import random 

updated_list = []

for site in sites:
    updated_list.append(site)
    response = requests.get(site)
    soup = BeautifulSoup(response.content, 'html.parser')
    href_links = []
    for link in soup.find_all('a'):
        if link.get('href'):
            if link.get("href")[0] == '/':
                href_links.append(link.get("href"))
    
    if len(href_links) > 10:
        random.shuffle(href_links)
        updated_list.extend(href_links[:2])