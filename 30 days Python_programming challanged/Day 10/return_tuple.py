def find_min_max(numbers):
    # Check if the list is empty
    if not numbers:
        return None, None
    
    # Initialize variables to store the smallest and largest numbers
    smallest = largest = numbers[0]
    
    # Iterate through the list to find the smallest and largest numbers
    for num in numbers:
        if num < smallest:
            smallest = num
        elif num > largest:
            largest = num
    
    # Return a tuple containing the smallest and largest numbers
    return smallest, largest

# Ask the user to input a list of numbers
numbers_list = input("Enter a list of numbers separated by spaces: ").split()

# Convert the input strings to integers
numbers_list = [int(num) for num in numbers_list]

# Call the function and get the result
min_num, max_num = find_min_max(numbers_list)

# Print the result
if min_num is not None and max_num is not None:
    print("Smallest number:", min_num)
    print("Largest number:", max_num)
else:
    print("The list is empty.")
