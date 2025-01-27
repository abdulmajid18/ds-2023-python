import heapq


def insert_with_priority_queue(intervals, newInterval):
    # Step 1: Add all intervals and newInterval into the heap
    heap = intervals + [newInterval]
    heapq.heapify(heap)

    result = []
    while heap:
        interval = heapq.heappop(heap)
        if not result or result[-1][1] < interval[0]:
            # No overlap, add to result
            result.append(interval)
        else:
            # Overlap, merge intervals
            result[-1][1] = max(result[-1][1], interval[1])

    return result


def insert_interval(intervals, newInterval):
    res = []

    for i in range(len(intervals)):
        if newInterval[1] < intervals[i][0]:
            res.append(newInterval)
            return res + intervals[i:]
        elif newInterval[0] > intervals[i][1]:
            res.append((intervals[i]))
        else:
            newInterval = [min(newInterval[0], intervals[i][0], max(newInterval[1], intervals[i][1]))]
    res.append(newInterval)
    return res
