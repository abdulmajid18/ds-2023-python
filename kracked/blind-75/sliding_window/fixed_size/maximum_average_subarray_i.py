from typing import List


def findMaxAverageOptimal(nums: List[int], k: int) -> float:
    l = 0
    runningSum = 0
    maxAvg = float("-inf")

    for r in range(len(nums)):
        runningSum += nums[r]
        curLength = (r - l) + 1
        if curLength == k:
            avg = runningSum / k
            maxAvg = max(avg, maxAvg)
            runningSum -= nums[l]
            l += 1
    return maxAvg
