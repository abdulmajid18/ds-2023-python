from typing import List


def findMaxLengthBruteForce(nums: List[int]) -> int:
    n = len(nums)
    max_len = 0

    for i in range(n):
        zeros = ones = 0
        for j in range(i, n):
            if nums[j] == 0:
                zeros += 1
            else:
                ones += 1

            if zeros == ones:
                max_len = max(max_len, j - i + 1)

    return max_len


from typing import List


def findMaxLength(nums: List[int]) -> int:
    balance_map = {0: -1}
    balance = 0
    max_len = 0

    for i, val in enumerate(nums):
        # Treat 1 as +1, and 0 as -1
        balance += 1 if val == 1 else -1

        if balance in balance_map:
            # The subarray between balance_map[balance] + 1 to i has net zero balance
            max_len = max(max_len, i - balance_map[balance])
        else:
            balance_map[balance] = i

    return max_len
