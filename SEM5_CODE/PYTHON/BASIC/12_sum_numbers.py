limit = int(input("Enter the last number: "))  # Read the last number
total = 0                                      # Store the running total

for number in range(1, limit + 1):             # Visit numbers from 1 to limit
    total = total + number                     # Add the current number

print("Sum:", total)                           # Display the total
