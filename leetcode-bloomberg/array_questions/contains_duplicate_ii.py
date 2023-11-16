def containsNearbyDuplicate(nums, k):
    # Create a dictionary to store the indices of elements
    index_dict = {}

    # Iterate through the array
    for i, num in enumerate(nums):
        # Check if the element is already in the dictionary
        if num in index_dict and abs(i - index_dict[num]) <= k:
            return True
        # Update the index of the current element in the dictionary
        index_dict[num] = i

    # If no such indices are found, return false
    return False
