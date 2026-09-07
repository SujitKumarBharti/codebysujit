import math                                  # Import factorial function


def calculate_sum(number):                   # Calculate the required series sum
    total = 1                                # Start with the first term
    for value in range(1, number + 1):       # Add terms from 1 to n
        total += 1 / math.factorial(value)   # Add 1 divided by value factorial
    return total                             # Return the sum


number = int(input("Enter n: "))             # Read the last term number
print("Series sum:", calculate_sum(number))  # Display the result
