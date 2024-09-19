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
