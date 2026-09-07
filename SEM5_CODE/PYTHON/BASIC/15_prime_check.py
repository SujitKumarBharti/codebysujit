number = int(input("Enter a number: "))  # Read the number
is_prime = True                          # Assume the number is prime

if number < 2:                           # Check numbers smaller than two
    is_prime = False                     # Mark the number as not prime
else:
    for divisor in range(2, number):     # Try possible divisors
        if number % divisor == 0:        # Check exact divisibility
            is_prime = False             # Mark the number as not prime
            break                        # Stop after finding a divisor

if is_prime:                             # Check the final result
    print("Prime number")                # Display prime result
else:
    print("Not a prime number")          # Display non-prime result
