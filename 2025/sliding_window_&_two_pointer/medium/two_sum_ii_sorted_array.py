from typing import List

from typing import List

class SolutionBrute:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            for j in range(i + 1, n):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]  # Return 1-based indices
        return []


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            cur_sum = numbers[l] + numbers[r]

            if cur_sum > target:
                r -= 1
            elif cur_sum < target:
                l += 1
            else:
                return l+1, r+1