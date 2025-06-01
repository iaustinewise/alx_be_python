#!/usr/bin/env python3
# Draw a square pattern using nested while and for loops

# Prompt user for the pattern size
size = int(input("Enter the size of the pattern: "))

# Use a while loop to iterate through rows
row = 1
while row <= size:
    # Use a for loop to print asterisks in each row
    for col in range(size):
        print("*", end="")
    # Move to the next line after each row
    print()
    row += 1
