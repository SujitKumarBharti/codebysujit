first = int(input("Enter first number: "))    # Read first number
second = int(input("Enter second number: "))  # Read second number
third = int(input("Enter third number: "))    # Read third number

if first >= second and first >= third:        # Check whether first is largest
    largest = first                           # Store first number
elif second >= first and second >= third:     # Check whether second is largest
    largest = second                          # Store second number
else:
    largest = third                           # Store third number

print("Largest number is:", largest)          # Display the largest number
