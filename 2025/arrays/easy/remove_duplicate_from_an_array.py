def remove_duplicates(arr):
    """
    Removes duplicates in place from a sorted array.

    Time Complexity: O(n), where n is the size of the array.
    Space Complexity: O(1), as we use no extra space (in-place modification).

    Arguments:
    arr : List[int] : Sorted input array of integers

    Returns:
    int : New length of the array after removing duplicates.

    Example:
    >>> remove_duplicates([1, 1, 2])
    2
    >>> remove_duplicates([0, 0, 1, 1, 1, 2, 2])
    3
    """

    if not arr:
        return 0  # If the array is empty, return 0

    # Pointer to track the position for unique elements
    i = 0

    # Start from the second element and check with the previous one
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]

    # The length of the array after removing duplicates
    return i + 1


# Example Test Cases
arr1 = [1, 1, 2]
k1 = remove_duplicates(arr1)
print(k1, arr1[:k1])  # Output: 2 [1, 2]

arr2 = [0, 0, 1, 1, 1, 2, 2]
k2 = remove_duplicates(arr2)
print(k2, arr2[:k2])  # Output: 3 [0, 1, 2]


def remove_duplicates_set(arr):
    """
    Removes duplicates in place from a sorted array using a HashSet.

    Time Complexity: O(n), where n is the size of the array.
    Space Complexity: O(n), as we are using a HashSet to store unique elements.

    Arguments:
    arr : List[int] : Sorted input array of integers

    Returns:
    int : New length of the array after removing duplicates.
    """

    # Create a HashSet to store unique elements
    unique_elements = set()

    # Traverse through the array and add elements to the HashSet
    for num in arr:
        unique_elements.add(num)

    # Copy the unique elements back into the array
    arr[:] = list(unique_elements)

    # The length of the unique elements is the new size of the array
    return len(unique_elements)

# Example Test Cases
arr1 = [1, 1, 2]
k1 = remove_duplicates(arr1)
print(k1, arr1[:k1])  # Output: 2 [1, 2]

arr2 = [0, 0, 1, 1, 1, 2, 2]
k2 = remove_duplicates(arr2)
print(k2, arr2[:k2])  # Output: 3 [0, 1, 2]
