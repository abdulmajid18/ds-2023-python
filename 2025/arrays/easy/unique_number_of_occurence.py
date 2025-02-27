from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import Counter
        freq = Counter(arr)
        return len(set(freq.values())) == len(freq.values())

