# Define two dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Merge the dictionaries
merged_dict = dict1.copy()  # Make a copy of dict1
merged_dict.update(dict2)   # Update with the contents of dict2

# Print the merged dictionary
print("Merged dictionary:")
print(merged_dict)
