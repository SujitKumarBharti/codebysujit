first_number = float(input("Enter first number: "))    # Read the first number
second_number = float(input("Enter second number: "))  # Read the second number

addition = first_number + second_number                # Add the numbers
subtraction = first_number - second_number             # Subtract the numbers
multiplication = first_number * second_number          # Multiply the numbers

print("Addition:", addition)                           # Display the addition
print("Subtraction:", subtraction)                     # Display the subtraction
print("Multiplication:", multiplication)               # Display the multiplication
if second_number != 0:                                 # Check before dividing
    division = first_number / second_number            # Divide the numbers
    print("Division:", division)                       # Display the division
else:
    print("Division is not possible by zero")          # Display the error
