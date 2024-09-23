def moveZeroesBruteForce1(nums):
    for i in range(len(nums)):
        if nums[i] == 0:
            nums.remove(0)
            nums.append(0)
    return nums


def moveZeroesBrute(nums):
    non_zero_elements = []
    zero_elements = []

    # Separate non-zero and zero elements
    for num in nums:
        if num != 0:
            non_zero_elements.append(num)
        else:
            zero_elements.append(num)

    # Concatenate non-zero elements followed by zeros
    nums[:] = non_zero_elements + zero_elements

    return nums


def moveZeroes(nums):
    non_zero_index = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[non_zero_index] = nums[non_zero_index], nums[i]
            non_zero_index += 1
    return nums
