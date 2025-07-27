from collections import deque
from typing import List


def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    result = []
    window = deque()

    for i, num in enumerate(nums):
        # Remove elements that are outside the current window
        while window and window[0] < i - k + 1:
            window.popleft()

        # Remove elements smaller than the current number from the back
        while window and nums[window[-1]] < num:
            window.pop()

        # Add the current index to the window
        window.append(i)

        # Add the maximum element to the result for each valid window
        if i >= k - 1:
            result.append(nums[window[0]])

    return result


def maxSlidingWindowBruteForce(nums, k):
    n = len(nums)
    result = []
    for i in range(n - k + 1):
        window = nums[i:i + k]
        result.append(max(window))
    return result
