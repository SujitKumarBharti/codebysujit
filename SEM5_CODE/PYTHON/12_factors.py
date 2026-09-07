number = int(input("Enter a number: "))                  # Read the number

if number == 0:                                          # Check zero separately
    print("Every non-zero integer is a factor of zero")  # Display zero case
else:
    for value in range(1, abs(number) + 1):              # Test possible positive factors
        if number % value == 0:                          # Check divisibility
            print(value, end=" ")                        # Display the factor
    print()                                              # Move to the next line
