from typing import List


def threeSumBruteForce(nums):
    nums.sort()
    n = len(nums)
    result = set()

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    result.add((nums[i], nums[j], nums[k]))

    return [list(triplet) for triplet in result]


# Example usage
nums = [-1, 0, 1, 2, -1, -4]
print(threeSumBruteForce(nums))  # Output: [[-1, -1, 2], [-1, 0, 1]]

nums = []
print(threeSumBruteForce(nums))  # Output: []

nums = [0]
print(threeSumBruteForce(nums))  # Output: []


def threeSumOptimal1(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    n = len(nums)
    res = set()

    for i, v in enumerate(nums):
        if i > 0 and v == nums[i - 1]:
            continue
        l, r = i + 1, n - 1
        while l < r:
            sum = v + nums[l] + nums[r]
            if sum > 0:
                r -= 1
            elif sum < 0:
                l += 1
            else:
                res.add((v, nums[l], nums[r]))
                l += 1

    return [list(triplet) for triplet in res]


def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    n = len(nums)
    res = []

    for i, v in enumerate(nums):
        if i > 0 and v == nums[i - 1]:
            continue
        l, r = i + 1, n - 1
        while l < r:
            sum = v + nums[l] + nums[r]
            if sum > 0:
                r -= 1
            elif sum < 0:
                l += 1
            else:
                res.append([v, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return res
