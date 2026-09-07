first_number = float(input("Enter first number: "))    # Read the first number
second_number = float(input("Enter second number: "))  # Read the second number

if first_number >= second_number:                      # Compare both numbers
    largest = first_number                             # Store the first number
else:
    largest = second_number                            # Store the second number

print("Largest number:", largest)                      # Display the largest number
