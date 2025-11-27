# Accept a letter from the user
letter = input("Enter a letter: ")

# Convert to lowercase for easy checking
letter = letter.lower()

# Check if it is a vowel
if letter in ('a', 'e', 'i', 'o', 'u'):
    print("The letter is a vowel.")
else:
    print("The letter is not a vowel.")