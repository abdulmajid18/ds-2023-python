import heapq
from collections import Counter

from collections import defaultdict
from queue import PriorityQueue


class Compare:
    def __init__(self, freq, val):
        self.freq = freq
        self.val = val

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.val < other.val
        return self.freq > other.freq


def solve(arr):
    n = len(arr)
    mpp = defaultdict(int)
    for a in arr:
        mpp[a] += 1
    max_heap = PriorityQueue()
    for key, value in mpp.items():
        max_heap.put(Compare(value, key))

    i = 0
    while not max_heap.empty():
        item = max_heap.get()
        freq = item.freq
        val = item.val
        for _ in range(freq):
            arr[i] = val
            i += 1
    return arr


from collections import defaultdict
import heapq


class Compare2:
    def __init__(self, freq, val):
        self.freq = freq
        self.val = val

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.val > other.val  # Sort by value in decreasing order
        return self.freq < other.freq  # Sort by frequency in increasing order


def solve2(arr):
    n = len(arr)
    mpp = defaultdict(int)

    # Count the frequency of each element in the array
    for a in arr:
        mpp[a] += 1

    min_heap = []

    for key, value in mpp.items():
        # Push elements into the min-heap as instances of the Compare class
        heapq.heappush(min_heap, Compare(value, key))

    i = 0
    while min_heap:
        item = heapq.heappop(min_heap)
        freq = item.freq
        val = item.val
        for _ in range(freq):
            arr[i] = val
            i += 1

    return arr


vec = [2, 5, 2, 8, 5, 6, 8, 8]
# print(solve(vec))

if __name__ == "__main__":
    # Example usage:
    nums = [4, 2, 2, 8, 3, 3, 1]
    sorted_nums = solve(nums)
    print(sorted_nums)
    sorted_nums = solve2(nums)
    print(sorted_nums)
