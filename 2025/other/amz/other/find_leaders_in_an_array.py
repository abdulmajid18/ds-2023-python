from typing import List


class Solution:
    def leaders(self, nums: List[int]) -> List[int]:
        leaders = []

        for i in range(len(nums)):
            is_leader = True
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    is_leader = False
                    break
            if is_leader:
                leaders.append(nums[i])

        return leaders


# Example usage:
sol = Solution()
nums = [16, 17, 4, 3, 5, 2]
print(sol.leaders(nums))  # Output: [17, 5, 2]


class SolutionOptimal:
    def leaders(self, nums: List[int]) -> List[int]:
        leaders = []
        max_right = float('-inf')

        # Traverse the array from right to left
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] >= max_right:
                leaders.append(nums[i])
                max_right = nums[i]  # Update the max_right

        # Reverse the leaders list to return them in the correct order
        return leaders[::-1]