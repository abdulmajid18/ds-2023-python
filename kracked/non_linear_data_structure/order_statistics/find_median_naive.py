def kth_smallest_naive(arr, k):
    arr = arr.copy()  # avoid modifying original array
    for _ in range(k-1):
        cur_smallest = 0
        for j in range(len(arr)):
            if arr[j] < arr[cur_smallest]:
                cur_smallest = j
        arr[cur_smallest] = float("inf")

    # Final smallest is the kth element
    cur_smallest = arr[0]
    for j in range(len(arr)):
        if arr[j] < cur_smallest:
            cur_smallest = arr[j]
    return cur_smallest


def find_median_naive(arr):
    n = len(arr)
    if n % 2 == 1:  # odd length
        return kth_smallest_naive(arr, n // 2 + 1)
    else:  # even length → average of middle two
        mid1 = kth_smallest_naive(arr, n // 2)
        mid2 = kth_smallest_naive(arr, n // 2 + 1)
        return (mid1 + mid2) / 2


arr1 = [7, 10, 4, 3, 20, 15]   # even
arr2 = [7, 10, 4, 3, 20]       # odd

print("Median of {} is: {}".format(arr1, find_median_naive(arr1)))
print("Median of {} is: {}".format(arr2, find_median_naive(arr2)))
