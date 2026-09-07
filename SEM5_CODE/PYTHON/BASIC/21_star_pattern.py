size = int(input("Enter a size: "))  # Read the number of lines

for line in range(1, size + 1):      # Create each pattern line
    stars = ""                       # Start with an empty line
    for count in range(line):        # Add stars one by one
        stars = stars + "*"          # Add one star
    print(stars)                     # Display the pattern line
