""" Given a sorted integer array where the range of elements are [0, 99] inclusive, return its
missing ranges """
from itertools import pairwise
from typing import List


class Solution:
    def get_range(self, start, end):
        if start == end:
            return str(start)
        return str(start) + "->" + str(end)

    def find_ranges(self, elements, start, end):
        ranges = []
        prev = start - 1
        for i in range(len(elements)):
            if i == len(elements):
                cur = end + 1
            else:
                cur = elements[i]
            if cur - prev >= 2:
                ranges.append(self.get_range(prev + 1, start - 1))
            prev = cur
        return ranges


class Solution2:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        def f(a, b):
            return str(a) if a == b else f'{a}->{b}'

        n = len(nums)
        if n == 0:
            return [f(lower, upper)]
        ans = []
        if nums[0] > lower:
            ans.append(f(lower, nums[0] - 1))
        for a, b in pairwise(nums):
            if b - a > 1:
                ans.append(f(a + 1, b - 1))
        if nums[-1] < upper:
            ans.append(f(nums[-1] + 1, upper))
        return ans


def main():
    solution = Solution2()
    elements = [0, 1, 3, 50, 75]
    for a, b in pairwise(elements):
        print(f"a ---> {a}    b ----> {b}")
    # ranges = solution.findMissingRanges(elements, 0, 99)
    # print(ranges)


if __name__ == '__main__':
    main()
