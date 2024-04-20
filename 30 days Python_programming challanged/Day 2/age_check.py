# Prompt the user to enter their age
age = int(input("Enter your age: "))

# Check if the age is even or odd
if age % 2 == 0:
    print("Your age, {}, is an even number.".format(age))
else:
    print("Your age, {}, is an odd number.".format(age))
