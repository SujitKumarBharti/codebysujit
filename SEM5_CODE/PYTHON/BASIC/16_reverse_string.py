text = input("Enter a string: ")             # Read the string
reverse_text = ""                            # Store the reversed string

for character in text:                       # Read every character
    reverse_text = character + reverse_text  # Add the character at the beginning

print("Reverse:", reverse_text)              # Display the reversed string
