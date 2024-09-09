def findPeakElement(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        # If mid element is greater than the next element, peak is on the left side
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            # Peak is on the right side
            left = mid + 1

    # left == right is the peak position
    return left
