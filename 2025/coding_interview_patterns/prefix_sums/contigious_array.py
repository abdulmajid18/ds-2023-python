from typing import List


def findMaxLengthBruteForce(nums: List[int]) -> int:
    n = len(nums)
    max_len = 0

    for i in range(n):
        zeros = 0
        ones = 0
        for j in range(i, n):
            if nums[j] == 0:
                zeros += 1
            else:
                ones += 1

            if zeros == ones:
                max_len = max(max_len, j - i + 1)
    return max_len


from typing import List


def findMaxLengthOptimized(nums: List[int]) -> int:
    # Replace 0 with -1 to use sum trick
    sum_index_map = {0: -1}
    max_len = 0
    running_sum = 0

    for i, num in enumerate(nums):
        running_sum += 1 if num == 1 else -1

        if running_sum in sum_index_map:
            max_len = max(max_len, i - sum_index_map[running_sum])
        else:
            sum_index_map[running_sum] = i

    return max_len