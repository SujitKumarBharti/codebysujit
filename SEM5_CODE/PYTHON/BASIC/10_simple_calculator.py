first_number = float(input("Enter first number: "))    # Read the first number
operator = input("Enter operator (+, -, *, /): ")      # Read the operator
second_number = float(input("Enter second number: "))  # Read the second number

if operator == "+":                                    # Check for addition
    result = first_number + second_number              # Add the numbers
elif operator == "-":                                  # Check for subtraction
    result = first_number - second_number              # Subtract the numbers
elif operator == "*":                                  # Check for multiplication
    result = first_number * second_number              # Multiply the numbers
elif operator == "/" and second_number != 0:           # Check for valid division
    result = first_number / second_number              # Divide the numbers
else:
    result = "Invalid operation"                       # Store an error message

print("Result:", result)                               # Display the result
