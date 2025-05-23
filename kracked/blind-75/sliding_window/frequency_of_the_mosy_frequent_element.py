def maxFrequency(nums, k):
    nums.sort()
    left = 0
    total = 0
    max_freq = 0

    for right in range(len(nums)):
        total += nums[right]

        while (right - left + 1) * nums[right] - total > k:
            total -= nums[left]
            left += 1

        max_freq = max(max_freq, right - left + 1)

    return max_freq


def maxFrequency2(nums, k):
    nums.sort()
    left = 0
    max_freq = 0
    current_cost = 0

    for right in range(len(nums)):
        if right > 0:
            current_cost += (nums[right] - nums[right - 1]) * (right - left)

        while current_cost > k:
            current_cost -= nums[right] - nums[left]
            left += 1

        max_freq = max(max_freq, right - left + 1)

    return max_freq

