from typing import List

def maxSubArrayTwo(self, nums: List[int]) -> int:
        curr_sum = max_sum = nums[0]

        for n in nums[1:]:
            curr_sum = max(n, curr_sum + n)
            max_sum = max(max_sum, curr_sum)

        return max_sum

def maxSubArray(nums: List[int]) -> int:
    maxSub = nums[0]
    curSum = 0

    for n in nums:
        if curSum < 0:
            curSum = 0
        curSum += n
        maxSub = max(maxSub, curSum)
    return maxSub

def maxSubArrayBruteForce(self, nums: List[int]) -> int:
    n = len(nums)
    ans = nums[0]

    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += nums[j]
            ans = max(ans, curr_sum)

    return ans