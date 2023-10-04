import heapq


def car_pooling(trips, capacity):
    # sort based on start
    trips.sort(key=lambda t: t[1])

    minHeap = []  # (start, numPass)
    cur_pass = 0

    for t in trips:
        num_pass, start, end = t

        while minHeap and minHeap[0][0] <= start:
            cur_pass -= minHeap[0][1]
            heapq.heappop(minHeap)
        cur_pass += num_pass
        if cur_pass > capacity:
            return False
        heapq.heappush(minHeap, [end, num_pass])
        return True


def car_pooling_two_efficient(trips, capacity):
    pass_change = [0] * 1000

    for t in trips:
        num_pass, start, end = t
        pass_change[start] += num_pass
        pass_change[end] -= num_pass

    cur_pass = 0
    for i in range(1000):
        cur_pass += pass_change[i]
        if cur_pass > capacity:
            return False
    return True
