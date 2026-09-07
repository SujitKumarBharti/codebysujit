number = int(input("Enter a number: "))          # Read the table number

for multiplier in range(1, 11):                  # Generate multipliers from 1 to 10
    result = number * multiplier                 # Calculate the table value
    print(number, "x", multiplier, "=", result)  # Display the table line
