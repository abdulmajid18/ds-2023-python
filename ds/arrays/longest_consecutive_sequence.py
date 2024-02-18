def longest_consecutive_brute(nums):
    if not nums:
        return 0

    nums.sort()  # Step 1
    max_length = 1
    current_length = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:  # Ignore duplicates
            if nums[i] == nums[i - 1] + 1:  # Check if current number is consecutive
                current_length += 1
            else:
                max_length = max(max_length, current_length)  # Update max length
                current_length = 1  # Reset current length

    return max(max_length, current_length)  # Step 4


# Example usage:
nums = [100, 4, 200, 1, 3, 2]
print(longest_consecutive_brute(nums))  # Output: 4


def longest_consecutive(nums):
    num_set = set(nums)
    max_length = 0

    for num in num_set:
        if num - 1 not in num_set:  # Check if num is the start of a sequence
            current_num = num
            current_length = 1

            while current_num + 1 in num_set:  # Iterate through consecutive numbers
                current_num += 1
                current_length += 1

            max_length = max(max_length, current_length)

    return max_length


# Example usage:
nums = [100, 4, 200, 1, 3, 2]
print(longest_consecutive(nums))  # Output: 4
