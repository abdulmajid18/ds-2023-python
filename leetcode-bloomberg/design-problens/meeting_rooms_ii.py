from typing import List


class Interval:
    def __int__(self, start, end):
        self.start = start
        self.end = end


def max_meeting_rooms(intervals: List[Interval]):
    start = sorted([i.start for i in intervals])
    end = sorted([i.end for i in intervals])

    res, count = 0, 0
    s, e = 0, 0

    while s < len(intervals):
        if start[s] < end[e]:
            s += 1
            count += 1
        else:
            e += 1
            count -= 1
        res = max(res, count)

    return res


