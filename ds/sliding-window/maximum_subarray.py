def max_subarray_bruteforce(nums):
    if not nums:
        return 0

    max_sum = float('-inf')

    for i in range(len(nums)):
        current_sum = 0
        for j in range(i, len(nums)):
            current_sum += nums[j]
            max_sum = max(max_sum, current_sum)

    return max_sum

# Example usage:
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray_bruteforce(nums)
print(result)

def max_subarray_n3(nums):
    if not nums:
        return 0

    n = len(nums)
    max_sum = float('-inf')

    for i in range(n):
        for j in range(i, n):
            current_sum = 0
            for k in range(i, j + 1):
                current_sum += nums[k]
            max_sum = max(max_sum, current_sum)

    return max_sum

# Example usage:
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray_n3(nums)
print(result)


def max_subarray1(nums):
    if not nums:
        return 0

    max_sum  = nums[0]
    current_sum = 0

    for n in nums:
        if current_sum < 0:
            current_sum = 0
        current_sum += n
        max_sum = max(max_sum, current_sum)
    return max_sum

# Example usage:
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray1(nums)
print(result)


def max_subarray(nums):
    if not nums:
        return 0

    max_sum = current_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

# Example usage:
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray(nums)
print(result)

