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


def findMinTwo(nums):
    res = nums[0]
    i, j = 0, len(nums) - 1

    while i <= j:
        # If the current subarray is already sorted
        if nums[i] < nums[j]:
            res = min(res, nums[i])
            break

        m = (i + j) // 2
        res = min(res, nums[m])

        # Narrow down the search space
        if nums[m] >= nums[i]:
            i = m + 1  # Move to the right half
        else:
            j = m - 1  # Move to the left half

    return res


class Solution:
    def findMin(self, nums):
        i, j = 0, len(nums) - 1

        # If the array is not rotated (or has only one element), return the first element
        if nums[j] >= nums[i]:
            return nums[i]

        # Binary search to find the minimum element
        while i < j:
            k = i + (j - i) // 2
            if nums[k] >= nums[0]:
                i = k + 1
            else:
                j = k

        return nums[i]
