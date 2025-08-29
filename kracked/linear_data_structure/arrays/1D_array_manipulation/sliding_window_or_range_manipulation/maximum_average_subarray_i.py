from typing import List


def findMaxAverageBruteForce(nums: List[int], k: int) -> float:
    max_avg = float('-inf')

    for i in range(len(nums) - k + 1):
        cur_window = nums[i:k + 1]

        cur_avg = sum(cur_window) / k

        max_avg = max(cur_avg, max_avg)

    return max_avg


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

