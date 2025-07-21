from typing import List

def triplet_sum_brute_force(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    triplets = set()

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                    triplets.add(triplet)

    return [list(triplet) for triplet in triplets]


def threeSum(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    nums.sort()
    result = []

    def pair_sum(nums, start, target):
        b, c = start, len(nums) - 1
        pairs = []

        while b < c:
            cur_sum = nums[b] + nums[c]
            if cur_sum == target:
                pairs.append([nums[b], nums[c]])
                b += 1
                while b < c and nums[b] == nums[b - 1]:
                    b += 1
            elif cur_sum < target:
                b += 1
            else:
                c -= 1
        return pairs

    for a in range(n):
        if nums[a] > 0:
            break
        if a > 0 and nums[a] == nums[a - 1]:
            continue
        pairs = pair_sum(nums, a + 1, -nums[a])
        for pair in pairs:
            result.append([nums[a]] + pair)
    return result

