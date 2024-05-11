def square_number(num):
    """
    Function to calculate the square of a number.

    Parameters:
        num (int or float): The number whose square is to be calculated.

    Returns:
        int or float: The square of the input number.
    """
    return num ** 2

# Test the function
number = float(input("Enter a number: "))  # You can input an integer or a float
result = square_number(number)
print(f"The square of {number} is: {result}")
