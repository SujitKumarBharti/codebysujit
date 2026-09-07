number = int(input("Enter a number: "))                     # Read the number
factorial = 1                                               # Store the factorial result

if number < 0:                                              # Check for a negative number
    print("Factorial is not defined for negative numbers")  # Display the error
else:
    for value in range(1, number + 1):                      # Visit values from 1 to number
        factorial = factorial * value                       # Multiply the current value
    print("Factorial:", factorial)                          # Display the factorial
