# Given lists
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# Use set() to remove duplicates and find common elements
common = list(set(a) & set(b))

# Print the result
print("Common elements:", common)