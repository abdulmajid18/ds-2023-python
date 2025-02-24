from typing import List


class SolutionBruteForce:
    def maxSubArrayOne(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = float('-inf')  # Initialize with negative infinity

        for i in range(n):  # Start index of subarray
            for j in range(i, n):  # End index of subarray
                current_sum = sum(nums[i:j + 1])  # Sum of subarray from i to j
                max_sum = max(max_sum, current_sum)  # Update max sum

        return max_sum

    def maxSubArrayTwo(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = float('-inf')

        for i in range(n):
            current_sum = 0  # Track sum of subarray starting at i
            for j in range(i, n):
                current_sum += nums[j]  # Incrementally sum subarray
                max_sum = max(max_sum, current_sum)

        return max_sum


class SolutionOptimized:
    def maxSubArraOne(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub

    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        current_sum = 0

        for num in nums:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum