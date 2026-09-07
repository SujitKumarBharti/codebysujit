terms = int(input("Enter number of terms: "))  # Read the number of terms
first = 0                                      # Store the first Fibonacci number
second = 1                                     # Store the second Fibonacci number

for count in range(terms):                     # Generate the required terms
    print(first, end=" ")                      # Display the current term
    next_number = first + second               # Calculate the next Fibonacci number
    first = second                             # Move the second number to first
    second = next_number                       # Move the next number to second
print()                                        # Move to the next line
