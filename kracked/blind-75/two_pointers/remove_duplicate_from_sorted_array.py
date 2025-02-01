def remove_duplicate_in_sorted_array(nums):
    l = 0  # slow pointer

    for r in range(1, len(nums)):  # start fast pointer from index 1
        if nums[l] != nums[r]:  # found a unique element
            l += 1  # increment the slow pointer
            nums[l] = nums[r]  # move unique element to the left

    return l+1  # return the subarray with unique elements


def removeDuplicates(nums):
    if not nums:
        return 0  # If the array is empty, return 0

    l = 1  # Slow pointer starts at index 1

    for r in range(1, len(nums)):  # Fast pointer starts from index 1
        if nums[r] != nums[r - 1]:  # Compare with previous element
            nums[l] = nums[r]  # Move unique element to the left
            l += 1  # Increment slow pointer

    return l  # Return the number of unique elements
