class RangeSum:
    def __init__(self, arr):
        n = len(arr)
        self.prefix = [0] * (n + 1)
        for i in range(n):
            self.prefix[i+1] = self.prefix[i] + arr[i]

    def sum_between(self, L, R):
        # L, R inclusive, 0 ≤ L ≤ R < n
        return self.prefix[R+1] - self.prefix[L]

from typing import List

class SumBetweenRange:
    def __init__(self, nums: List[int]):
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sum_range(self, i: int, j: int) -> int:
        return self.prefix[j+1] - self.prefix[i]
