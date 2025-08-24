def kth_smallest_sorting(arr, k):
    # Step 1: Sort array in O(n log n)
    arr_sorted = sorted(arr)
    # Step 2: Return the (k-1)th index (since 0-based indexing)
    return arr_sorted[k-1]


arr = [7, 10, 4, 3, 20, 15]
k = 3
print("The {}th smallest element is: {}".format(k, kth_smallest_sorting(arr, k)))
