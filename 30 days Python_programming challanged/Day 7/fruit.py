def main():
    # Create an empty list to store fruits
    fruits = []

    # Prompt the user to enter 5 fruits
    for i in range(5):
        fruit = input("Enter a fruit: ")
        fruits.append(fruit)

    # Print each fruit using a for loop
    print("Fruits you entered:")
    for fruit in fruits:
        print(fruit)

# Call the main function to execute the program
if __name__ == "__main__":
    main()
