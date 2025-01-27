def longest_increasing_subsequence(nums):
    LIS = [1] * len(nums)

    for i in range(len(nums), -1, -1):
        for j in range(i+1, len(nums)):
            if nums[i] < nums[j]:
                LIS[i] = max(LIS[i], 1 + LIS[j])
    return max(LIS)


def lengthOfLIS(nums):
    n = len(nums)
    dp = [1] * n  # Each element is its own LIS initially

    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


from bisect import bisect_left


def lengthOfLIS(nums):
    q = []  # To maintain the increasing subsequence

    for num in nums:
        pos = bisect_left(q, num)  # Find the first position >= num
        if pos == len(q):
            q.append(num)  # Append if num is larger than all in q
        else:
            q[pos] = num  # Replace to maintain the tight sequence

    return len(q)
