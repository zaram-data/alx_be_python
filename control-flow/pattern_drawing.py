# pattern_drawing.py

# Ask the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# While loop to go through each row
while row < size:
    # For loop to print stars in each row
    for col in range(size):
        print("*", end="")  # Print star without moving to next line
    print()  # Move to the next line after a row is done
    row += 1  # Move to the next row
