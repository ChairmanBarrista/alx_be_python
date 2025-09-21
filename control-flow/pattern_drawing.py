# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Draw the pattern using while loop and nested for loop
row = 0
while row < size:
    col = 0
    for col in range(size):
        print("*", end="")
    print()  # Newline after each row
    row += 1
