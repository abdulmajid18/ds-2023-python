def canAttendMeetings(intervals):
    intervals.sort(key=lambda x: x[0])
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False
    return True


def canAttendMeetings2(intervals):
    intervals.sort(key=lambda x: x[0])
    for i in range(1, len(intervals)):
        i1 = intervals[i - 1]
        i2 = intervals[i]

        if i1[1] > i2[0]:
            return False
    return True


def minMeetingRooms(intervals):
    events = []

    # Create a list of start and end events
    for interval in intervals:
        events.append((interval[0], 1))  # Meeting starts
        events.append((interval[1], -1))  # Meeting ends

    # Sort events by time. If times are the same, process end (-1) first
    events.sort(key=lambda x: (x[0], x[1]))

    count = 0
    max_rooms = 0

    # Process the events
    for event in events:
        count += event[1]  # Increment or decrement the count

        # Track the maximum number of rooms needed
        max_rooms = max(max_rooms, count)

    return max_rooms
