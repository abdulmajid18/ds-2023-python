import heapq


def heap_sort(arr):
    heapq.heapify(arr)

    sorted_arr = [heapq.heappop(arr) for _ in range(len(arr))]

    return sorted_arr


nums = [10, 7, 8, 9, 1, 5]
sorted_nums = heap_sort(nums.copy())
print("Sorted array:", sorted_nums)
