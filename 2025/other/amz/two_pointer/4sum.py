from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate values
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:  # Skip duplicate values
                    continue

                l, r = j + 1, n - 1  # Two pointers

                while l < r:
                    total = nums[i] + nums[j] + nums[l] + nums[r]

                    if total == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])

                        while l < r and nums[l] == nums[l + 1]:  # Skip duplicates
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:  # Skip duplicates
                            r -= 1

                        l += 1
                        r -= 1

                    elif total < target:
                        l += 1
                    else:
                        r -= 1

        return res


from typing import List


class SolutionBruteForce:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = set()  # Using a set to avoid duplicates

        # Generate all quadruplets using four nested loops
        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                for k in range(j + 1, n - 1):
                    for l in range(k + 1, n):
                        if nums[i] + nums[j] + nums[k] + nums[l] == target:
                            res.add(tuple(sorted([nums[i], nums[j], nums[k], nums[l]])))  # Store as a sorted tuple

        return list(map(list, res))  # Convert set of tuples back to list of lists
