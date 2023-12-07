def minMeetingRooms(intervals):
    if not intervals:
        return 0

    start_times = sorted([interval[0] for interval in intervals])
    end_times = sorted([interval[1] for interval in intervals])

    rooms = 0
    endPointer = 0

    for i in range(len(intervals)):
        if start_times[i] >= end_times[endPointer]:
            endPointer += 1
        else:
            rooms += 1

    return rooms


def minMeetingRooms2(intervals):
    if not intervals:
        return 0

    start_times = sorted([interval[0] for interval in intervals]) 
    end_times = sorted([interval[1] for interval in intervals])

    res, count = 0, 0
    s, e = 0, 0

    while s < e:
        if start_times[s] < end_times[e]:
            s += 1
            count += 1
        else:
            e += 1
            count -= 1
        res = max(res, count)
    return res


import heapq


def minMeetingRoomsHeapsEfficient(intervals):
    if not intervals:
        return 0

    # Sort the intervals by start time
    intervals.sort(key=lambda x: x[0])

    # Create a min-heap to store end times of meetings
    end_times = []
    heapq.heappush(end_times, intervals[0][1])

    rooms = 1  # At least one room is needed for the first meeting

    for i in range(1, len(intervals)):
        start_time, end_time = intervals[i]

        # If the current meeting can reuse a room, remove the earliest end time from the heap
        if start_time >= end_times[0]:
            heapq.heappop(end_times)

        # Add the end time of the current meeting to the heap
        heapq.heappush(end_times, end_time)

        # The size of the heap represents the number of rooms in use at the current time
        rooms = max(rooms, len(end_times))

    return rooms
