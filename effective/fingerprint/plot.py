# data = {"None": 17.57,
# "adblock": 16.57,
# "ublock": 15.99,
# "privacy-badger": 17.57,
# "decentraleyes": 15.57,
# "disconnect": 15.25,
# "ghostery": 14.99,
# "https": 14.77,
# "noscript": 13.99,
# "canvas-antifp": 17.57,
# "adguard": 14.57,
# "user-agent": 14.4}

import matplotlib.pyplot as plt

# Customizing the x-axis ticks
x_ticks = [12, 14, 16, 18, 20]

base_value = 10

# Provided data
labels = ["None", "ABP", "UbO", "PB", "Decentraleyes", "Disconnect", 
          "Ghostery", "Https Everywhere", "NS", "CFD", "AdG", "UA Switcher"]
values = [17.57, 16.57, 15.99, 17.57, 15.57, 15.25, 14.99, 14.77, 13.99, 17.57, 14.57, 14.4]
uniqueness = ['Unique', "Nearly-Unique", "Nearly-Unique", "Unique", "Nearly-Unique", "Nearly-Unique", "Nearly-Unique", "Nearly-Unique", "Partial Protection", "Unique", "Nearly-Unique", "Nearly-Unique"]

adjusted_values = [value - base_value for value in values]

usenix_font = {'fontname':'Times New Roman'} 

# Setting global font family
plt.rcParams['font.family'] = 'Times New Roman'

size = 18
# Plotting the bar char
# t with customized fonts and sizes
plt.figure(figsize=(8,8))
bars = plt.barh(labels, values, color='royalblue')
plt.xlabel('Bits of Information', fontsize=size)
# plt.ylabel('Extensions', fontsize=size)
plt.xlim(12,18)

# Add text on the right side of each bar
i = 0
for bar, original_value in zip(bars, values):
    width = bar.get_width()
    plt.text(width + 0.1, bar.get_y() + bar.get_height() / 2, uniqueness[i], fontsize=size, ha='left', va='center')
    i += 1

# plt.title('Bar Chart of Extensions vs Values', fontsize=size)
plt.xticks(x_ticks, fontsize=16)
plt.yticks(fontsize=16)
plt.grid(axis='x', which='both', linestyle='--', linewidth=0.5)

# Display the plot
plt.show()
# plt.savefig('fingerprint.pdf')