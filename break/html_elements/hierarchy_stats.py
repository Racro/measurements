import json

def calculate_statistics(numbers):
    total = sum(numbers)
    length = len(numbers)
    average = total / length

    sorted_numbers = sorted(numbers)
    middle_index = length // 2

    median = sorted_numbers[middle_index] if length % 2 != 0 else (sorted_numbers[middle_index - 1] + sorted_numbers[middle_index]) / 2

    return f"""
        'mean': {average},
        'median': {median},
        'min': {min(numbers)},
        'max': {max(numbers)},
        'range': {max(numbers) - min(numbers)},
        'count': {length}
    """

with open('hierarchy/buttons_control.json') as file:
    data_dict = json.load(file)

change_lst = []
for site in data_dict.keys():
    for html_code, count in data_dict[site]:
        if count and count.isdigit(): 
            change_lst.append(int(count))

statistics = calculate_statistics(change_lst)
print(statistics)


import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = {'A': [1, 2, 3, 4, 5], 'B': [10, 15, 7, 12, 9]}

# Creating a box plot using Seaborn
sns.boxplot(data=data)
plt.xlabel('Category')
plt.ylabel('Values')
plt.title('Box Plot')
plt.show()
