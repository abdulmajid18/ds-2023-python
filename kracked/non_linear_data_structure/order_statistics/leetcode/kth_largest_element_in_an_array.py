
import heapq

def kth_largest_in_an_array(arr, k):
    max_heap = []

    for num in arr:
        heapq.heappush(max_heap, -num)

    res = None
    for _ in range(k - 1):
        heapq.heappop(max_heap)

    return -heapq.heappop(max_heap)

def kth_largest_in_an_array_heapify(arr, k):
    max_heap = [-num for num in arr]
    heapq.heapify(max_heap)
    for _ in range(k - 1):
        heapq.heappop(max_heap)
    return -heapq.heappop(max_heap)


import heapq

def kth_largest_in_an_array_two(arr, k):
    min_heap = []
    for num in arr:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return min_heap[0]


import random


def kth_largest_in_an_array_optimal(arr, k):
    target = len(arr) - k

    def partition(left, right, pivot_index):
        pivot_value = arr[pivot_index]
        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
        store_index = left

        for i in range(left, right):
            if arr[i] < pivot_value:
                arr[store_index], arr[i] = arr[i], arr[store_index]
                store_index += 1

        arr[right], arr[store_index] = arr[store_index], arr[right]
        return store_index

    def quickselect(left, right):
        if left == right:
            return arr[left]


        pivot_index = random.randint(left, right)
        pivot_index = partition(left, right, pivot_index)

        if pivot_index == target:
            return arr[pivot_index]
        elif pivot_index < target:
            return quickselect(pivot_index + 1, right)
        else:
            return quickselect(left, pivot_index - 1)

    return quickselect(0, len(arr) - 1)
