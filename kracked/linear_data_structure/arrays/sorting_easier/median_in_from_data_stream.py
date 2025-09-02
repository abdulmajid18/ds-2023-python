import heapq

class MedianFinder:

    def __init__(self):
        self.low = []   # max-heap (store negatives)
        self.high = []  # min-heap

    def addNum(self, num: int) -> None:
        # Push to max-heap first
        heapq.heappush(self.low, -num)

        # Ensure every num in low <= every num in high
        if self.low and self.high and -self.low[0] > self.high[0]:
            heapq.heappush(self.high, -heapq.heappop(self.low))

        # Balance sizes
        if len(self.low) > len(self.high) + 1:
            heapq.heappush(self.high, -heapq.heappop(self.low))
        if len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def findMedian(self) -> float:
        if len(self.low) > len(self.high):
            return -self.low[0]  # top of max-heap
        return (-self.low[0] + self.high[0]) / 2