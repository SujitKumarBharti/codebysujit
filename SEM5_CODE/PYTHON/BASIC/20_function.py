def greet(name):                        # Define a greeting function
    message = "Hello, " + name          # Create the greeting message
    return message                      # Return the message


user_name = input("Enter your name: ")  # Read the user's name
result = greet(user_name)               # Call the function
print(result)                           # Display the returned message
