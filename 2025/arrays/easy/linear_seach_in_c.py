# Function to perform Linear Search
def linear_search(arr, num):
    # Traverse through all elements of the array
    for i in range(len(arr)):
        # If element is found
        if arr[i] == num:
            return i  # Return the index of the element
    return -1  # If element is not found, return -1

# Example usage:
arr = [1, 2, 3, 4, 5]
num = 3  # Element to be searched

# Call the linear_search function
result = linear_search(arr, num)

if result != -1:
    print(f"Element found at index: {result}")  # If found, print index
else:
    print("Element not found.")
