def moveZeroes(nums):
    # Initialize a variable to count the number of non-zero elements
    non_zero_count = 0

    # Iterate through the array
    for i in range(len(nums)):
        # If the current element is non-zero, move it to the appropriate position
        if nums[i] != 0:
            nums[non_zero_count], nums[i] = nums[i], nums[non_zero_count]
            non_zero_count += 1


# Example usage:
nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)
