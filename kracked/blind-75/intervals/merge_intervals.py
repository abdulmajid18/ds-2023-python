class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

def merge_intervals_A(intervals):
    events = []

    # Step 1: Create event points
    for start, end in intervals:
        events.append((start, +1))  # Start of an interval
        events.append((end, -1))   # End of an interval

    # Step 2: Sort events by time, and prioritize +1 over -1 when times are equal
    events.sort(key=lambda x: (x[0], x[1]))

    merged = []
    active_intervals = 0
    start = None

    # Step 3: Traverse the events
    for time, event_type in events:
        if active_intervals == 0:  # Start of a merged interval
            start = time

        active_intervals += event_type  # Update the active interval count

        if active_intervals == 0:  # End of a merged interval
            merged.append([start, time])

    return merged


# def mergeInterval(intervals):
#     intervals.sort(key=lambda i: i.end)
#
#     for
