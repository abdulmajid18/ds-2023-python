def findMin(nums):
    """
    Find the minimum element in a rotated sorted array.

    Args:
    nums (List[int]): A rotated sorted array.

    Returns:
    int: The minimum element in the array.
    """
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        # If the middle element is greater than the rightmost element,
        # the minimum must be in the right half.
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            # Otherwise, the minimum is in the left half (including mid).
            right = mid

    # At the end of the loop, left == right, pointing to the minimum element.
    return nums[left]
