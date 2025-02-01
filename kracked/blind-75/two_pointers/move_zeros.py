def moveZeroes(nums):
    temp = []  # Step 1: Store non-zero elements
    for num in nums:
        if num != 0:
            temp.append(num)

    # Step 2: Fill with zeroes
    temp.extend([0] * (len(nums) - len(temp)))

    # Step 3: Copy back to original array
    for i in range(len(nums)):
        nums[i] = temp[i]

# Example
nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]
