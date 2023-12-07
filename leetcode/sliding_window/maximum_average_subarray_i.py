"""
You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the
maximum average value and return this value. Any answer with a calculation error
less than 10-5 will be accepted.

"""
from typing import List


def findMaxAverage(self, nums: List[int], k: int) -> float:
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


def find_max_average(nums, k):
    window_start, window_sum = 0, 0.0
    max_avg = float('-inf')

    for window_end in range(len(nums)):
        # Add the incoming element to the window sum
        window_sum += nums[window_end]
        # If we've hit the window size, start sliding
        if window_end >= k - 1:
            # Calculate average of current window and compare with max_avg
            max_avg = max(max_avg, window_sum / k)
            # Subtract the outgoing element from window sum
            window_sum -= nums[window_start]
            # Slide the window
            window_start += 1

    return max_avg
