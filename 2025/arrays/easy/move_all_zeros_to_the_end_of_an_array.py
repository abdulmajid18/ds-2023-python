def move_zeros_brute(arr):
    """
    Moves all zeros in the array to the end while maintaining the relative order of non-zero elements.

    Time Complexity: O(n), where n is the number of elements in the array.
    Space Complexity: O(n), due to the temporary array used.

    Parameters:
    arr (List[int]): The input array to modify.
    """

    # Count the number of non-zero elements
    non_zero_elements = [num for num in arr if num != 0]

    # Calculate the number of zeros
    zeros_count = len(arr) - len(non_zero_elements)

    # Rebuild the array: first add non-zero elements, then add zeros
    arr[:] = non_zero_elements + [0] * zeros_count  # Modify the original array in place


# Example Usage:
arr1 = [0, 1, 0, 3, 12]
move_zeros_brute(arr1)
print(arr1)  # Output: [1, 3, 12, 0, 0]


def move_zeros_in_place(arr):
    """
    Moves all zeros in the array to the end while maintaining the relative order of non-zero elements,
    using the two pointer approach in-place.

    Time Complexity: O(n), where n is the number of elements in the array.
    Space Complexity: O(1), since no extra array is used.

    Parameters:
    arr (List[int]): The input array to modify.
    """

    j = 0  # Pointer to track where to place the next non-zero element

    # Traverse the array with i
    for i in range(len(arr)):
        if arr[i] != 0:
            # Swap non-zero element with arr[j]
            arr[i], arr[j] = arr[j], arr[i]
            j += 1  # Move the pointer to the next position


# Example Usage:
arr = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
move_zeros_in_place(arr)
print(arr)  # Output: [1, 2, 3, 2, 4, 5, 1, 0, 0, 0]
