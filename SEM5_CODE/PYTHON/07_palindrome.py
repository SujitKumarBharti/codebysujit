def is_palindrome(text):                         # Check whether text reads the same backward
    reverse_text = ""                            # Start with an empty reverse string
    for character in text:                       # Read each character in order
        reverse_text = character + reverse_text  # Add character at the beginning
    return text == reverse_text                  # Compare text with its reverse


text = input("Enter a string: ")                 # Read the string
if is_palindrome(text):                          # Check the result
    print("Palindrome")                          # Display palindrome
else:
    print("Not a palindrome")                    # Display non-palindrome
