numbers = [5, 10, 15, 20, 25]  # Create a list of numbers
total = 0                      # Store the running total

for number in numbers:         # Visit every list item
    print(number)              # Display the current item
    total = total + number     # Add the current item

print("List sum:", total)      # Display the total
