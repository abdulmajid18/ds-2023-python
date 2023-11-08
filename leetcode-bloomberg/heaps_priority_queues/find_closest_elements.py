import heapq

def findClosestElements(arr, k, x):
    min_heap = []  # Create a min-heap to store the closest elements

    for num in arr:
        distance = abs(num - x)

        # Push elements into the heap with distance as the key
        # Keep a maximum of k elements in the heap
        if len(min_heap) < k:
            heapq.heappush(min_heap, (-distance, num))
        else:
            # If the heap is full, pop the element with the largest distance
            if distance < -min_heap[0][0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, (-distance, num))

    result = [num for (_, num) in min_heap]

    # Sort the result in ascending order
    result.sort()

    return result
