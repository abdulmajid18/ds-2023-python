class SolutionBruteForce:
    def threeSum(self, nums):
        n = len(nums)
        result = set()  # Using a set to store unique triplets

        # Iterate through all triplets (i, j, k)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = tuple(sorted([nums[i], nums[j], nums[k]]))  # Sort to avoid duplicates
                        result.add(triplet)  # Store only unique triplets

        return list(result)  # Convert set to list for output


class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:  # Skip duplicate elements
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                total = num + nums[l] + nums[r]  # Sum of triplet
                if total > 0:
                    r -= 1  # Move right pointer left (reduce sum)
                elif total < 0:
                    l += 1  # Move left pointer right (increase sum)
                else:
                    res.append([num, nums[l], nums[r]])  # Found a valid triplet
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:  # Skip duplicates
                        l += 1

        return res
