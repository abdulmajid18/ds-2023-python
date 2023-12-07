def max_sum_subarray(arr, k):
    # Compute sum of the first window of size k
    # arr[:k] slices the array from index 0 to k
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        # Compute sum of next window of size k by
        # removing the first element of the previous
        # window and adding the next element
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)

    return max_sum