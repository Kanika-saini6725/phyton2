# Ask the user for a number
num = int(input("Enter a number: "))

# Create an empty list to store divisors
divisors = []

# Check all numbers from 1 to num
for i in range(1, num + 1):
    if num % i == 0:   # If remainder is 0, it's a divisor
        divisors.append(i)

# Print the list of divisors
print("The divisors of", num, "are:", divisors)