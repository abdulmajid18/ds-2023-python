def search_insert_brute_force(nums, target):
    """
    Finds the index of the target in a sorted array.
    If not found, returns the index where it should be inserted.

    Approach:
    - Iterate through the array to find the first index where nums[i] >= target.
    - If target is larger than all elements, return len(nums).

    Time Complexity: O(n) (Worst-case: traversing the entire array)
    Space Complexity: O(1) (No extra space used)

    Parameters:
    - nums (List[int]): A sorted list of distinct integers.
    - target (int): The target value.

    Returns:
    - int: The index where target is found or should be inserted.
    """
    for i in range(len(nums)):
        if nums[i] >= target:
            return i
    return len(nums)  # If target is greater than all elements


# Test Cases
print(search_insert_brute_force([1, 3, 5, 6], 5))  # Output: 2
print(search_insert_brute_force([1, 3, 5, 6], 2))  # Output: 1
print(search_insert_brute_force([1, 3, 5, 6], 7))  # Output: 4
print(search_insert_brute_force([1, 3, 5, 6], 0))  # Output: 0
print(search_insert_brute_force([1], 2))  # Output: 1


def search_insert(nums, target):
    """
    Given a sorted array of distinct integers and a target value, returns the index
    if the target is found. If not, returns the index where it would be inserted.

    Uses Binary Search for O(log n) time complexity.

    Parameters:
    - nums (List[int]): A sorted list of distinct integers.
    - target (int): The target value to search for.

    Returns:
    - int: The index where target is found or should be inserted.
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid  # Found target, return index
        elif nums[mid] < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half

    return left  # Left will be the insert position


# Test Cases
print(search_insert([1, 3, 5, 6], 5))  # Output: 2
print(search_insert([1, 3, 5, 6], 2))  # Output: 1
print(search_insert([1, 3, 5, 6], 7))  # Output: 4
print(search_insert([1, 3, 5, 6], 0))  # Output: 0
print(search_insert([1], 2))  # Output: 1
