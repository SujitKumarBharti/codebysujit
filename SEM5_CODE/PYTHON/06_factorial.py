def factorial(number):                                      # Calculate factorial of a number
    result = 1                                              # Store the product
    for value in range(1, number + 1):                      # Multiply all values up to number
        result *= value                                     # Update the product
    return result                                           # Return the factorial


number = int(input("Enter a number: "))                     # Read the number
if number < 0:                                              # Check for a negative input
    print("Factorial is not defined for negative numbers")  # Display the error
else:
    print("Factorial:", factorial(number))                  # Display the factorial
