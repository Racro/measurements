import os
from difflib import SequenceMatcher

f = open('filterlist/exceptionrules.txt', 'r')
accept_ads = f.readlines()
f.close()

path = "./filterlist/ublock_filters/"
dir_list = os.listdir(path)

rules = []
for file in dir_list:
    f = open(path+file, 'r')
    rules.extend(f.readlines())
    f.close()

# strip rules into two parts -> rules_allowed (with the @@), rules_blocked 
rules_allowed = []
rules_blocked = []
for rule in rules:
    if rule.startswith('@@||'):
        domain = rule.split('@@||')[1]
        domain = domain.split('?')[0]       
        domain = domain.split('$')[0]
        domain = domain.split('^')[0]         
        rules_allowed.append(domain)
    elif rule.startswith('||'):
        domain = rule.split('||')[1]
        domain = domain.split('?')[0]       
        domain = domain.split('$')[0]
        domain = domain.split('^')[0]
        rules_blocked.append(domain)

# strip accept_ads to include only domains
rules_exception = []
for rule in accept_ads:
    if rule.startswith('@@||'):
        domain = rule.split('@@||')[1]
        domain = domain.split('?')[0]
        domain = domain.split('$')[0]        
        domain = domain.split('^')[0]        
        rules_exception.append(domain)

f = open('conflicts.txt', 'w')
count = 0
print(len(rules_exception))
print(len(rules_blocked))

match_list = []
for exception in rules_exception:
    for rule in rules_blocked:
        match = os.path.commonprefix([exception, rule])
        # print(exception)
        # print(rule)
        if (len(match) > 7):
            print(match)
            match = match.split('/')[0]
            if match not in match_list:
                if match[-1] == '/':
                    match_list.append(match)
                    match_list.append(match[:-1])
                else:
                    match_list.append(match)
                    # match_list.append(match+'/')
                count += 1
                f.write(f'{match} for {exception}')
                f.write('\n')
            break
            
#     print(f'count: {count}')

# f.write(f'Total conflicts: {count}')
# f.close()

# print(f'Total conflicts: {count}')
count = 0
for match in match_list:
    for rule in rules_allowed:
        mat = os.path.commonprefix([exception, rule])
        if len(mat) == len(match):
            count += 1
print(count)