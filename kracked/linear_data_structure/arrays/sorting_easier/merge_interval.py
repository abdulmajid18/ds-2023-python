from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            prev_start, prev_end = res[-1]
            curr_start, curr_end = intervals[i]

            if curr_start <= prev_end:
                res[-1][1] = max(prev_end, curr_end)
            else:
                res.append(intervals[i])

        return res



