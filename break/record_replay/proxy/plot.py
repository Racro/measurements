import matplotlib.pyplot as plt
import json

f = open('avg_range_data.json', 'r')
your_data_dict = json.load(f)
f.close()
# Replace 'your_data_dict' with your actual data dictionary

# Creating a figure and axis for each key
fig, axs = plt.subplots(4, 1, figsize=(10, 20))

# Looping through the dictionary and plotting each line graph
for i, (key, values) in enumerate(your_data_dict.items()):
    # if key == 'javascript':
    #     print(values)
    # Sorting the values
    sorted_values = sorted(values)
    axs[i].plot(sorted_values)
    axs[i].set_title(key)
    axs[i].set_xlabel("Index")
    axs[i].set_ylabel("Value")

# Adjusting layout for better spacing
plt.tight_layout()

# Displaying the plots
plt.show()
