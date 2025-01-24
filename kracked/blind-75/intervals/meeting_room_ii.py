from typing import List
import heapq

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


def minMeetingRooms(intervals):
    if not intervals:
        return 0

    # Step 1: Sort intervals by start time
    intervals.sort(key=lambda x: x[0])

    # Step 2: Min-Heap to track end times
    import heapq
    min_heap = []

    for interval in intervals:
        # If the earliest ending meeting ends before the current meeting starts, remove it
        if min_heap and min_heap[0] <= interval[0]:
            heapq.heappop(min_heap)

        # Add the current meeting's end time to the heap
        heapq.heappush(min_heap, interval[1])

    # Step 3: The size of the heap is the number of meeting rooms needed
    return len(min_heap)
