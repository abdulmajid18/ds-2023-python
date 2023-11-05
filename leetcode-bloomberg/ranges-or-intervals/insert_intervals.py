def insertInterval(intervals, newInterval):

    res = []
    for i in range(intervals):
        start, stop = intervals[i]
        if start > newInterval[1]:
            res.append(newInterval)
            return res + intervals[i:]
        elif stop < newInterval[0]:
            res.append(intervals[i])
        else:
            newInterval = [min(newInterval[0], start),
                           max(newInterval[1], stop)]
    res.append(newInterval)
    return res
