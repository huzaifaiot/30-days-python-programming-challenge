# Define a list of tuples
list_of_tuples = [(3, 'apple'), (1, 'banana'), (2, 'orange'), (4, 'grape')]

# Sort the list of tuples by the second item in each tuple
sorted_list = sorted(list_of_tuples, key=lambda x: x[1])

# Print the sorted list
print("Sorted list of tuples by the second item:")
for item in sorted_list:
    print(item)
