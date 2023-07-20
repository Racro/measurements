import json
import matplotlib.pyplot as plt
import numpy as np

f = open('href_count.json', 'r')
d = json.load(f)
f.close()

a = [0]*60

for site in d.keys():
    if (d[site] > 200):
        continue
    a[int(d[site]/5)] += 1

a = np.array(a)
print(a)

plt.plot(a)
plt.show()
