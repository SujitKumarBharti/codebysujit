class Stack:                         # Create a stack using a list
    def __init__(self):              # Initialize the stack
        self.items = []              # Store stack items

    def push(self, item):            # Add an item to the top
        self.items.append(item)      # Insert the item

    def pop(self):                   # Remove the top item
        if self.is_empty():          # Check whether stack has no items
            return "Stack is empty"  # Report empty stack
        return self.items.pop()      # Remove and return top item

    def peek(self):                  # View the top item
        if self.is_empty():          # Check whether stack has no items
            return "Stack is empty"  # Report empty stack
        return self.items[-1]        # Return top item

    def is_empty(self):              # Check whether stack is empty
        return len(self.items) == 0  # Return the empty status

    def display(self):               # Display all stack items
        print(self.items)            # Print the list


stack = Stack()                      # Create a stack object
stack.push(10)                       # Push the first item
stack.push(20)                       # Push the second item
stack.push(30)                       # Push the third item
stack.display()                      # Display the stack
print("Peek:", stack.peek())         # Display the top item
print("Pop:", stack.pop())           # Remove and display the top item
stack.display()                      # Display the updated stack
