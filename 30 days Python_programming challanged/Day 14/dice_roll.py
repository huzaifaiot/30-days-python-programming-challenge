import random

def roll_dice():
    """Simulate a dice roll."""
    return random.randint(1, 6)

# Roll the dice
result = roll_dice()

# Print the result
print("The dice rolled:", result)
