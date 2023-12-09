
def three_sum_brute_force(nums):
    result = []
    nums.sort()

    result = []
    nums.sort()

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # Skip duplicates
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = [nums[i], nums[j], nums[k]]
                    result.append(triplet)

    return result


# Example usage:
nums = [-1, 0, 1, 2, -1, -4]
result = three_sum_brute_force(nums)
print(result)  # Output: [[-1, -1, 2], [-1, 0, 1]]


def threeSum(nums):
    res = []

    nums.sort()
    for i, a in enumerate(nums):
        if i > 0 and a == nums[i-1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            threeSum = a + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                res.append([a, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l-1]  and l < r:
                    l += 1
    return res

