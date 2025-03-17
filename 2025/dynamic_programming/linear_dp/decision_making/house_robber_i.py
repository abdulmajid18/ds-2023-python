from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2


def rob(nums):
    if not nums:
        return 0

    prev1, prev2 = 0, 0  # Initialize two variables to track max money robbed

    for num in nums:
        new_rob = max(prev1, prev2 + num)  # Either rob this house or skip it
        prev2 = prev1  # Move prev2 to previous max
        prev1 = new_rob  # Move prev1 to current max

    return prev1  # Maximum money that can be robbed


# Test cases
print(rob([1, 2, 3, 1]))  # Output: 4
print(rob([2, 7, 9, 3, 1]))  # Output: 12
