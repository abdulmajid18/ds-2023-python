def numSubarraysWithSumBrute(nums: list[int], goal: int) -> int:
    count = 0
    n = len(nums)

    for i in range(n):
        sum_ = 0
        for j in range(i, n):
            sum_ += nums[j]
            if sum_ == goal:
                count += 1

    return count


from collections import defaultdict


def numSubarraysWithSum(nums: list[int], goal: int) -> int:
    prefix_count = defaultdict(int)
    prefix_count[0] = 1  # there's one way to have sum = 0 (empty prefix)

    prefix_sum = 0
    result = 0

    for num in nums:
        prefix_sum += num

        # if prefix_sum - goal exists, we found a valid subarray
        result += prefix_count[prefix_sum - goal]

        # update prefix count
        prefix_count[prefix_sum] += 1

    return result
