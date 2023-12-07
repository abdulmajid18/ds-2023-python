from collections import deque


def sliding_window_maximum(nums, k):
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


# Example usage:
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
result = sliding_window_maximum(nums, k)
print(result)
