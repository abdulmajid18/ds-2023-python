def minMeetingRooms(intervals):
    if not intervals:
        return 0

    # Separate out the start and end times
    start_times = sorted([i[0] for i in intervals])
    end_times = sorted([i[1] for i in intervals])

    # Pointers for start_times and end_times
    start_pointer = 0
    end_pointer = 0

    # Number of rooms needed and max_rooms used at any point
    rooms_needed = 0
    max_rooms = 0

    # Iterate over the start times
    while start_pointer < len(intervals):
        if start_times[start_pointer] < end_times[end_pointer]:
            # A meeting is starting, so we need a new room
            rooms_needed += 1
            start_pointer += 1
        else:
            # A meeting ended, so we free up a room
            rooms_needed -= 1
            end_pointer += 1

        # Track the maximum number of rooms needed at any point
        max_rooms = max(max_rooms, rooms_needed)

    return max_rooms


def minMeetingRooms2(intervals):
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
