def linear_search(items, target):                            # Search each list item in order
    for index in range(len(items)):                          # Visit every index
        if items[index] == target:                           # Check the current item
            return index                                     # Return the matching index
    return -1                                                # Return -1 when target is absent


def binary_search(items, target):                            # Search a sorted list by halves
    left = 0                                                 # Set the first index
    right = len(items) - 1                                   # Set the last index
    while left <= right:                                     # Continue while a range remains
        middle = (left + right) // 2                         # Find the middle index
        if items[middle] == target:                          # Check the middle item
            return middle                                    # Return the matching index
        if items[middle] < target:                           # Check whether target is on the right
            left = middle + 1                                # Discard the left half
        else:
            right = middle - 1                               # Discard the right half
    return -1                                                # Return -1 when target is absent


items = [2, 5, 8, 12, 16, 20]                                # Create a sorted list
target = int(input("Enter a value to search: "))             # Read the target
print("Linear search index:", linear_search(items, target))  # Display linear result
print("Binary search index:", binary_search(items, target))  # Display binary result
