def lengthOfLIS(nums):
    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n  # Initialize dp array to 1, as LIS at each position is at least the element itself.

    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)  # The length of the longest subsequence is the maximum value in dp array.
