def findDisappearedNumbers(nums):
    # Create a set of the given numbers
    num_set = set(nums)

    # Initialize a list to store missing numbers
    missing_numbers = []

    # Iterate through the range [1, n]
    for i in range(1, len(nums) + 1):
        # If the current number is not in the set, it is missing
        if i not in num_set:
            missing_numbers.append(i)

    return missing_numbers


nums = [4, 3, 2, 7, 8, 2, 1]
result = findDisappearedNumbers(nums)
print(result)  # Output: [5, 6]

nums = [1, 1]
result = findDisappearedNumbers(nums)
print(result)  # Output: [2]

nums = [2, 2]
result = findDisappearedNumbers(nums)
print(result)  # Output: [1]
