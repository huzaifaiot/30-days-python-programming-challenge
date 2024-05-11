def is_palindrome(word):
    # Convert the word to lowercase
    word = word.lower()
    
    # Compare the original word with its reverse
    return word == word[::-1]

# Test the function
word = input("Enter a word to check if it's a palindrome: ")
if is_palindrome(word):
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")
