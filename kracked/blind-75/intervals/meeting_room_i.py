class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


def canAttendMeeting(intervals):
    intervals.sort(key=lambda i: i.start)

    # prev
    for i in range(1, len(intervals)):
        i1 = intervals[i - 1]
        i2 = intervals[i]

        if i1.end > i2.start:
            return False

    return True


def minMeetingRooms(intervals):
    events = []

    # Step 1: Create events
    for start, end in intervals:
        events.append((start, 1))  # Meeting starts
        events.append((end, -1))  # Meeting ends

    # Step 2: Sort events
    events.sort(key=lambda x: (x[0], x[1]))

    # Step 3: Traverse and count
    count = 0
    max_rooms = 0
    for _, value in events:
        count += value
        max_rooms = max(max_rooms, count)

    return max_rooms
