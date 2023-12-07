from typing import List


class Interval:
    def __int__(self, start, end):
        self.start = start
        self.end = end


def can_attend_meeting(intervals: List[Interval]):
    intervals.sort(key=lambda i: i.start)

    for i in range(1, len(intervals)):
        i1 = intervals[i - 1]
        i2 = intervals[i]

        if i1.end > i2.start:
            return False
    return True
