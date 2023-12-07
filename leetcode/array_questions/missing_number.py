def missingNumber(nums):
    n = len(nums)

    # Calculate the sum of the first n natural numbers using the formula n * (n + 1) / 2
    expected_sum = n * (n + 1) // 2

    # Calculate the sum of the elements in the array
    actual_sum = sum(nums)

    # The missing number is the difference between the expected sum and the actual sum
    missing_number = expected_sum - actual_sum

    return missing_number
