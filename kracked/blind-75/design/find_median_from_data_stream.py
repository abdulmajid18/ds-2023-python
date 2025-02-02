import heapq

class MedianFinder:
    def __init__(self):
        # Max heap for the smaller half
        self.small = []  # max-heap (we invert the values to use min-heap as max-heap)
        # Min heap for the larger half
        self.large = []  # min-heap

    def addNum(self, num: int) -> None:
        # Add to max heap (invert the value for max-heap behavior)
        heapq.heappush(self.small, -num)

        # Ensure max of small is <= min of large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Balance the sizes of the heaps
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]  # max of small
        return (-self.small[0] + self.large[0]) / 2  # average of max of small and min of large
