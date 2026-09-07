text = input("Enter a string: ")             # Read the string
reverse_text = ""                            # Store the reversed string

for character in text:                       # Read every character
    reverse_text = character + reverse_text  # Add the character at the beginning

if text == reverse_text:                     # Compare original and reversed strings
    print("Palindrome")                      # Display palindrome result
else:
    print("Not a palindrome")                # Display non-palindrome result
