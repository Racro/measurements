import json

benign = ['zillow', 'fandom', 'yahoo', 'opera', 'time.com', 'zdnet', 'softonic', 'gamespot', 'gogriz']

f = open('adblock_detect_custom.json', 'r')
d = json.load(f)
f.close()

print(f'keys: {d.keys()}')

for extn in d.keys():
    for site in d[extn]:
        for keyword in benign:
            if keyword in site[0]:
                d[extn].remove(site)

for extn in d.keys():
    print(f'{extn}: {len(d[extn])}')

    # if extn == 'adblock':
    #     print(extn)
    #     for site in range(len(d['adblock'])):
    #         print(d['adblock'][site][0])
    # if extn == 'control':
    #     print(extn)
    #     for site in range(len(d['control'])):
    #         print(d['control'][site][0])
    # print(f'{extn}: {len(d[extn])}')

# adblock:
# https://www.forbes.com/sites/tylerroush/2023/05/04/florida-likely-next-state-to-restrict-gender-affirming-care-here-are-all-the-states-with-similar-bans-or-restrictions/
# http://www.imgur.com
# http://www.wetransfer.com
# http://www.foxnews.com
# http://www.independent.co.uk/newsletters?itm_channel=native&itm_campaign=burger_nav&itm_audience=prospecting&itm_content=newsletters
# http://www.cbsnews.com
# https://www.latimes.com/world-nation/story/2023-05-04/coronation-time-a-bit-of-harry-potter-a-touch-of-monty-python-more-than-a-little-national-self-reckoning
# https://www.geeksforgeeks.org/introduction-to-recursion-data-structure-and-algorithm-tutorials/
# http://www.rottentomatoes.com
# https://www.history.com/topics/immigration/asian-american-timeline
# http://www.insider.com
# http://www.schooldigger.com
