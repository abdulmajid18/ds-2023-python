import heapq


def find_second_largest_and_smallest(n, a):
    # Max heap for second largest
    max_heap = [-x for x in a]  # Negate the numbers to simulate max heap
    heapq.heapify(max_heap)

    # Pop the largest element (most negative in the max heap)
    largest = -heapq.heappop(max_heap)

    # Pop the second-largest element
    second_largest = -heapq.heappop(max_heap)

    # Min heap for second smallest
    min_heap = a[:]
    heapq.heapify(min_heap)

    # Pop the smallest element
    smallest = heapq.heappop(min_heap)

    # Pop the second smallest element
    second_smallest = heapq.heappop(min_heap)

    return [second_largest, second_smallest]


# Example Test Case
n = 5
a = [1, 2, 3, 4, 5]
result = find_second_largest_and_smallest(n, a)
print(result)  # Output: [4, 2]
