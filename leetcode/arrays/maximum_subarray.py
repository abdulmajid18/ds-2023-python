def maximumSubarray(nums):
    maxSum = 0
    curSum = nums[0]

    for n in nums:
        if curSum < 0:
            curSum = 0
        curSum += n
        maxSum = max(maxSum, curSum)
    return maxSum