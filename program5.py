
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

sum = a + b + c

if a == b == c:
    sum = 3 * sum   # thrice of their sum

print("The result is:", sum)
