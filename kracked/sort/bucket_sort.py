def bucket_sort_0_1(arr):
    n = len(arr)
    if n == 0:
        return arr


    buckets = [[] for _ in range(n)]

    # Put array elements into buckets
    for num in arr:
        index = int(n * num)   # works if arr values in [0,1)
        if index == n:         # edge case for num == 1
            index = n - 1
        buckets[index].append(num)

    # Sort individual buckets (insertion sort or Python’s sort)
    for bucket in buckets:
        bucket.sort()

    # Concatenate results
    result = []
    for bucket in buckets:
        result.extend(bucket)

    return result

def bucket_sort_non_negative(arr):
    n = len(arr)
    if n == 0:
        return arr

    min_val, max_val = min(arr), max(arr)
    if min_val == max_val:
        return arr

    # Create n empty buckets
    buckets = [[] for _ in range(n)]

    # Distribute elements into buckets
    for x in arr:
        index = int((x - min_val) / (max_val - min_val + 1) * n)
        if index == n:   # edge case: max value
            index = n - 1
        buckets[index].append(x)

    # Sort each bucket
    for bucket in buckets:
        bucket.sort()

    # Concatenate buckets
    result = []
    for bucket in buckets:
        result.extend(bucket)

    return result

