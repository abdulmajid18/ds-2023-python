

def max_subarray(nums):
    max_sub = nums[0]
    cur_sum = 0

    for n in nums:
        if cur_sum < 0:
            cur_sum = 0
        cur_sum += n
        max_sub = max(max_sub, cur_sum)

    return max_sub