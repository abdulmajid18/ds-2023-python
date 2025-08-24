def partition(A, start, end):
    pivot = A[end]
    p_index = start

    for i in range(start, end):  # iterate through subarray
        if A[i] <= pivot:
            A[i], A[p_index] = A[p_index], A[i]
            p_index += 1


    A[p_index], A[end] = A[end], A[p_index]
    return p_index


def quick_sort(arr, start, end):
    if start < end:
        p_index = partition(arr, start, end)
        quick_sort(arr, start, p_index - 1)  # left side
        quick_sort(arr, p_index + 1, end)  # right side



arr = [7, 10, 4, 3, 20, 15]
quick_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
