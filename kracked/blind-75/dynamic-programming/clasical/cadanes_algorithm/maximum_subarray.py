from typing import List


def maxSubArrayBruteForce(self, nums: List[int]) -> int:
    max_sum = float('-inf')

    for i in range(len(nums)):
        for j in range(i, len(nums)):
            current_sum = sum(nums[i:j + 1])
            max_sum = max(max_sum, current_sum)

    return max_sum


def maxSubArrayBruteForceTwo(self, nums: List[int]) -> int:
    max_sum = float('-inf')
    n = len(nums)

    for i in range(n):
        current_sum = 0  # Initialize the sum for the current subarray starting at i
        for j in range(i, n):
            current_sum += nums[j]  # Add the current element to the running sum
            max_sum = max(max_sum, current_sum)  # Update max_sum if needed

    return max_sum

def maxSubArray(nums: List[int]) -> int:
    max_sum = float('-inf')
    current_max = 0
    for num in nums:
        current_max = max(current_max + num, num)
        max_sum = max(max_sum, current_max)

    return max_sum


def maxSubArray1(nums: List[int]) -> int:
    max_sum = nums[0]
    current_sum = 0

    for num in nums:
        if current_sum < 0:
            current_sum = 0
        current_sum += num

        max_sum = max(max_sum, current_sum)

    return max_sum