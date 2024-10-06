from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # Case 1: No overlap, newInterval is before the current interval
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]  # Add the remaining intervals as is

            # Case 2: No overlap, newInterval is after the current interval
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])

            # Case 3: Overlap detected, merge intervals
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        # If newInterval hasn't been added, add it at the end
        res.append(newInterval)
        return res
