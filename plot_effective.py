import numpy as np
import matplotlib.pyplot as plt
import json
import matplotlib.colors as mcolors

extensions = ['adblock', 'ublock', 'privacy-badger', "decentraleyes",
       "disconnect",
       "ghostery",
       "https",
       "noscript",
       "scriptsafe",
       "canvas-antifp",
       "adguard",
       "user-agent"]

extn_dict = {
    'adblock': 'ABP', 'ublock': 'UbO', 'privacy-badger': 'PB', "decentraleyes": 'Decentraleyes',
       "disconnect": 'Disconnect',
       "ghostery": 'Ghostery',
       "https": 'HTTPS Everywhere',
       "noscript": 'NoScript',
       "scriptsafe": 'ScriptSafe',
       "canvas-antifp": 'CFD',
       "adguard": 'AdG',
       "user-agent": 'UA Switcher'
}

frames = json.load(open('effective/ads/plot_frames.json', 'r'))
third_party = json.load(open('effective/third_party/plot_third_party.json', 'r'))

color_map = plt.cm.get_cmap('Set3', 12)

# Sample data (replace this with your 12 arrays of data)
x_values = np.arange(1, 13)  # Assuming you have 12 x-values from 1 to 12
data_arrays = []  # List to store your 12 arrays of data
for extn in extensions:
    # data = np.random.randn(10)  # Replace 10 with the number of data points in each array
    data_arrays.append(frames[extn])

# Calculate mean and standard deviation for each data array
means = [np.mean(data) for data in data_arrays]
std_devs = [np.std(data) for data in data_arrays]

# Set the positions of the dots (x-values)
x_positions = np.arange(1, len(means) + 1)

# Plot the scatter plot
sc = plt.scatter(x_positions, means, c=x_positions, label='Mean', cmap='Set1', s=50)
# Add error bars to the scatter plot
plt.errorbar(x_positions, means, yerr=std_devs, fmt='none', capsize=5, ecolor='black')

# # Set the positions of the bars
# x_positions = np.arange(len(means))
# # Create the bar plot
# plt.bar(x_positions, means, yerr=std_devs, capsize=5, color='lightblue', edgecolor='black', alpha=0.7)

# plt.xticks(x_positions, extensions)

# Set labels and title
plt.xlabel('Extensions')
plt.ylabel('Difference from control case (absolute)')
plt.title('Frames Plot with Mean and Standard Deviation')


num_extensions = len(extensions)
# Create a custom legend
legend_elements = [plt.Line2D([0], [0], color=color_map(i), lw=4, label=f'{extn_dict[extensions[i]]}') for i in range(num_extensions)]
# fig.legend(handles=legend_elements, prop={'size': 6}, loc='lower right', bbox_to_anchor=(0.96, 0.05), ncols=2)
plt.legend(handles=legend_elements, prop={'size': 6}, loc='lower right', bbox_to_anchor=(0.96, 0.05), ncols=1)

# Hide x-axis ticks
plt.xticks([])

# plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()