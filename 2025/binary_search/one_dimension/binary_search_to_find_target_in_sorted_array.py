from typing import List


def searcBruteForce(nums, target):
    # Iterate over each element with its index in the list.
    for index, num in enumerate(nums):
        if num == target:
            return index  # Return the index when the target is found.
    return -1  # Return -1 if the target is not found.


# Example usage:
nums1 = [-1, 0, 3, 5, 9, 12]
target1 = 9
print(searcBruteForce(nums1, target1))  # Expected Output: 4

nums2 = [-1, 0, 3, 5, 9, 12]
target2 = 2
print(searcBruteForce(nums2, target2))  # Expected Output: -1


def search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1  # Correctly initialize r

    while l <= r:
        mid = (l + r) // 2

        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
        else:
            return mid
    return -1


# Example usage:
nums1 = [-1, 0, 3, 5, 9, 12]
target1 = 9
print(search(nums1, target1))  # Output: 4

nums2 = [-1, 0, 3, 5, 9, 12]
target2 = 2
print(search(nums2, target2))  # Output: -1


def binarySearch(nums, low, high, target):
    # Base case: If the search space is invalid, target is not in the array.
    if low > high:
        return -1

    mid = (low + high) // 2  # Calculate the middle index.

    # If the middle element is the target, return its index.
    if nums[mid] == target:
        return mid
    # If target is greater than the middle element, search in the right half.
    elif target > nums[mid]:
        return binarySearch(nums, mid + 1, high, target)
    # Otherwise, search in the left half.
    else:
        return binarySearch(nums, low, mid - 1, target)


def search(nums, target):
    # Initial call to the recursive function with the full array as the search space.
    return binarySearch(nums, 0, len(nums) - 1, target)


# Example usage:
nums1 = [-1, 0, 3, 5, 9, 12]
target1 = 9
print(search(nums1, target1))  # Expected Output: 4

nums2 = [-1, 0, 3, 5, 9, 12]
target2 = 2
print(search(nums2, target2))  # Expected Output: -1
