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
