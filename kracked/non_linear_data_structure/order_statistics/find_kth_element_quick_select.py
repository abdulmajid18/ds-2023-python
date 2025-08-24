def partition(A, start, end):
    pivot = A[end]
    p_index = start

    for i in range(start, end):
        if A[i] <= pivot:
            A[i], A[p_index] = A[p_index], A[i]
            p_index += 1

    A[p_index], A[end] = A[end], A[p_index]
    return p_index


def quickselect(A, start, end, k):
    """
    Returns the k-th smallest element (1-based index).
    """
    if start <= end:
        p_index = partition(A, start, end)

        if p_index == k - 1:  # pivot is the k-th smallest
            return A[p_index]
        elif p_index > k - 1:  # k-th lies in left part
            return quickselect(A, start, p_index - 1, k)
        else:  # k-th lies in right part
            return quickselect(A, p_index + 1, end, k)
    return None


arr = [7, 10, 4, 3, 20, 15]
k = 3
result = quickselect(arr.copy(), 0, len(arr) - 1, k)
print("The {}th smallest element is: {}".format(k, result))
