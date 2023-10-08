def search_rotated_sorted_duplicates(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        m = (l + r) // 2
        if target == nums[m]:
            return m

        if nums[l] < nums[m]:
            if target > nums[m]:
                l = m + 1
            elif target < nums[l]:
                l = m + 1
            else:
                r = m - 1
        elif nums[l] > nums[m]:
            if target < nums[m]:
                r = m - 1
            elif target > nums[r]:
                r = m - 1
            else:
                l = m + 1
        else:
            l += 1
    return -1




def search(nums, target):
    return searchRecursive(nums, 0, len(nums) - 1, target)

def searchRecursive(nums, left, right, target):
    if left > right:
        return False

    mid = left + (right - left) // 2

    if nums[mid] == target:
        return True

    # Handle duplicates by moving the left pointer if nums[left] == nums[mid]
    while left < mid and nums[left] == nums[mid]:
        left += 1

    # Check if the left half is sorted
    if nums[left] <= nums[mid]:
        if nums[left] <= target < nums[mid]:
            return searchRecursive(nums, left, mid - 1, target)
        else:
            return searchRecursive(nums, mid + 1, right, target)
    else:
        # If left half is not sorted, search in the right half
        if nums[mid] < target <= nums[right]:
            return searchRecursive(nums, mid + 1, right, target)
        else:
            return searchRecursive(nums, left, mid - 1, target)

# Example usage:
nums = [2, 5, 6, 0, 0, 1, 2]
target = 0
print(search(nums, target))  # Output: True (target found in the rotated sorted array with duplicates)
