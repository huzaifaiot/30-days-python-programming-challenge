import random

def guess_number():
    # Generate a random number between 1 and 10
    target_number = random.randint(1, 10)
    
    while True:
        try:
            # Ask the user to guess the number
            guess = int(input("Guess a number between 1 and 10: "))
            
            # Check if the guess is correct
            if guess == target_number:
                print("Congratulations! You guessed it right!")
                break
            else:
                print("Wrong guess! Try again.")
        except ValueError:
            print("Please enter a valid number.")

# Call the function to start the game
guess_number()
