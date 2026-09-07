def gcd(first, second):                       # Calculate the greatest common divisor
    while second != 0:                        # Continue until the remainder is zero
        remainder = first % second            # Find the remainder
        first = second                        # Move the second number to first
        second = remainder                    # Move the remainder to second
    return abs(first)                         # Return a positive GCD


first = int(input("Enter first number: "))    # Read first number
second = int(input("Enter second number: "))  # Read second number
print("GCD:", gcd(first, second))             # Display the GCD
