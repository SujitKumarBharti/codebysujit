class Queue:                         # Create a queue using a list
    def __init__(self):              # Initialize the queue
        self.items = []              # Store queue items

    def enqueue(self, item):         # Add an item at the rear
        self.items.append(item)      # Insert the item

    def dequeue(self):               # Remove the front item
        if self.is_empty():          # Check whether queue has no items
            return "Queue is empty"  # Report empty queue
        return self.items.pop(0)     # Remove and return front item

    def front(self):                 # View the front item
        if self.is_empty():          # Check whether queue has no items
            return "Queue is empty"  # Report empty queue
        return self.items[0]         # Return front item

    def is_empty(self):              # Check whether queue is empty
        return len(self.items) == 0  # Return the empty status

    def display(self):               # Display all queue items
        print(self.items)            # Print the list


queue = Queue()                      # Create a queue object
queue.enqueue(10)                    # Add the first item
queue.enqueue(20)                    # Add the second item
queue.enqueue(30)                    # Add the third item
queue.display()                      # Display the queue
print("Front:", queue.front())       # Display the front item
print("Dequeue:", queue.dequeue())   # Remove and display the front item
queue.display()                      # Display the updated queue
