def is_sorted(arr):
    """
    Check if the array is sorted in ascending or non-decreasing order.

    Approach:
    - Iterate through the array and compare each element with the next.
    - If any element is greater than the next element, the array is not sorted.

    Time Complexity:
    - O(n), where n is the size of the array. The array is traversed once.

    Space Complexity:
    - O(1), as we are using a constant amount of space.

    Arguments:
    arr : List[int] : The input array of integers.

    Returns:
    bool : True if the array is sorted, False otherwise.

    Example:
    >>> is_sorted([1, 2, 2, 3, 4])
    True

    >>> is_sorted([1, 3, 2, 4])
    False
    """

    # Iterate through the array and check each element with the next
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False  # Array is not sorted if any element is greater than the next one

    return True  # If no such element was found, the array is sorted


def is_sorted_2(arr):
    """
    Check if the array is sorted in ascending or non-decreasing order.

    Approach:
    - Traverse the array and check if each element is greater than or equal to the previous one.
    - If any element is smaller than the previous one, the array is not sorted.

    Time Complexity:
    - O(n), where n is the size of the array. The array is traversed once.

    Space Complexity:
    - O(1), as we are using a constant amount of space.

    Arguments:
    arr : List[int] : The input array of integers.

    Returns:
    bool : True if the array is sorted, False otherwise.

    Example:
    >>> is_sorted_2([1, 2, 2, 3, 4])
    True

    >>> is_sorted_2([1, 3, 2, 4])
    False
    """

    # If the array has 0 or 1 element, it's trivially sorted
    if len(arr) <= 1:
        return True

    # Traverse through the array and check if the array is sorted
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False  # Return False if any element is smaller than the previous one

    return True  # If no violations were found, the array is sorted


# Example Test Cases
print(is_sorted([1, 2, 2, 3, 4]))  # Output: True
print(is_sorted([1, 3, 2, 4]))  # Output: False
print(is_sorted([10]))  # Output: True (Single element is trivially sorted)
print(is_sorted([5, 5, 5, 5]))  # Output: True (All equal elements, sorted)

# Example Test Cases
print(is_sorted([1, 2, 2, 3, 4]))  # Output: True
print(is_sorted([1, 3, 2, 4]))  # Output: False
print(is_sorted([10]))  # Output: True (Single element is trivially sorted)
print(is_sorted([5, 5, 5, 5]))  # Output: True (All equal elements, sorted)
