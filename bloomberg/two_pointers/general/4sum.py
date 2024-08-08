from typing import List


def fourSum(nums, target):
    nums.sort()  # Sort the array to facilitate pruning and use of two-pointer technique
    n = len(nums)
    quadruplets = []

    for h1 in range(n - 3):
        # Avoid duplicates for the first element
        if h1 > 0 and nums[h1] == nums[h1 - 1]:
            continue
        # Pruning: skip if the smallest possible sum with nums[h1] is greater than target
        if nums[h1] * 4 > target:
            break
        # Pruning: skip if the largest possible sum with nums[h1] is less than target
        if nums[h1] + nums[-1] * 3 < target:
            continue

        for h2 in range(h1 + 1, n - 2):
            # Avoid duplicates for the second element
            if h2 > h1 + 1 and nums[h2] == nums[h2 - 1]:
                continue
            # Pruning: skip if the smallest possible sum with nums[h1] and nums[h2] is greater than target
            if nums[h1] + 3 * nums[h2] > target:
                break
            # Pruning: skip if the largest possible sum with nums[h1] and nums[h2] is less than target
            if nums[h1] + nums[h2] + nums[-1] * 2 < target:
                continue

            left, right = h2 + 1, n - 1
            while left < right:
                total = nums[h1] + nums[h2] + nums[left] + nums[right]
                if total == target:
                    quadruplets.append([nums[h1], nums[h2], nums[left], nums[right]])
                    # Skip duplicates for the third element
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicates for the fourth element
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1

    return quadruplets


# Example usage:
nums = [1, 0, -1, 0, -2, 2]
target = 0
print(fourSum(nums, target))  # Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        quad = []
        n = len(nums)

        for h1 in range(n - 3):
            if h1 > 0 and nums[h1] == nums[h1 - 1]:
                continue
            if nums[h1] * 4 > target:
                break
            if nums[h1] + nums[-1] * 3 < target:
                continue

            for h2 in range(h1 + 1, n - 2):
                if h2 > h1 + 1 and nums[h2] == nums[h2 - 1]:
                    continue
                if nums[h1] + 3 * nums[h2] > target:
                    break
                if nums[h1] + nums[h2] + nums[-1] * 2 < target:
                    continue

                left, right = h2 + 1, n - 1
                while left < right:
                    total = nums[h1] + nums[h2] + nums[left] + nums[right]
                    if total == target:
                        quad.append([nums[h1], nums[h2], nums[left], nums[right]])

                        # Skip duplicates for the third element
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        # Skip duplicates for the fourth element
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        return quad

