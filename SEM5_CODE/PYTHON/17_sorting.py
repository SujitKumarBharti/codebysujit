def insertion_sort(items):                                                           # Sort using insertion sort
    result = items[:]                                                                # Copy the original list
    for index in range(1, len(result)):                                              # Select each item after the first
        current = result[index]                                                      # Store the selected item
        position = index - 1                                                         # Start comparing with the previous item
        while position >= 0 and result[position] > current:                          # Shift larger items
            result[position + 1] = result[position]                                  # Move the larger item right
            position -= 1                                                            # Move to the previous position
        result[position + 1] = current                                               # Insert the selected item
    return result                                                                    # Return the sorted list


def bubble_sort(items):                                                              # Sort using bubble sort
    result = items[:]                                                                # Copy the original list
    for end in range(len(result) - 1, 0, -1):                                        # Reduce the unsorted range
        for index in range(end):                                                     # Compare neighboring items
            if result[index] > result[index + 1]:                                    # Check item order
                result[index], result[index + 1] = result[index + 1], result[index]  # Swap items
    return result                                                                    # Return the sorted list


def selection_sort(items):                                                           # Sort using selection sort
    result = items[:]                                                                # Copy the original list
    for start in range(len(result)):                                                 # Select each starting position
        smallest = start                                                             # Assume the first item is smallest
        for index in range(start + 1, len(result)):                                  # Search the remaining items
            if result[index] < result[smallest]:                                     # Check for a smaller item
                smallest = index                                                     # Store the smaller item's index
        result[start], result[smallest] = result[smallest], result[start]            # Place smallest item
    return result                                                                    # Return the sorted list


items = [64, 25, 12, 22, 11]                                                         # Create an unsorted list
print("Original list:", items)                                                       # Display the original list
print("Insertion sort:", insertion_sort(items))                                      # Display insertion result
print("Bubble sort:", bubble_sort(items))                                            # Display bubble result
print("Selection sort:", selection_sort(items))                                      # Display selection result
