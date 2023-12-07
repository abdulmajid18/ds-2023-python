def singleNumber(nums):
    # Calculate the expected sum of all unique elements
    expected_sum = sum(set(nums)) * 2

    # Calculate the actual sum of the array
    actual_sum = sum(nums)

    # The difference between the expected and actual sums is the single element
    result = expected_sum - actual_sum

    return result


def singleNumberUsingXOR(nums):
    result = 0

    # XOR all elements in the array
    for num in nums:
        result ^= num

    return result
