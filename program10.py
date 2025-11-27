# Ask the user for a string
string = input("Enter a string: ")

# Reverse the string using slicing
reverse = string[::-1]

# Check if the string is equal to its reverse
if string == reverse:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")