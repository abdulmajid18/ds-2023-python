def counting_sort(A, k):
    """
    Counting Sort implementation.
    A: input list (values must be integers in [0..k])
    k: maximum value in A
    Returns a new sorted list B
    """
    n = len(A)
    B = [0] * n       # output array
    C = [0] * (k + 1) # counts array

    # Step 1: count frequencies
    for j in range(n):
        C[A[j]] += 1

    # Step 2: accumulate counts
    for i in range(1, k + 1):
        C[i] += C[i - 1]

    # Step 3: build output (stable sort, go backwards)
    for j in range(n - 1, -1, -1):
        B[C[A[j]] - 1] = A[j]
        C[A[j]] -= 1

    return B


def counting_sort_non_negative(arr):
    max_val = max(arr)

    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    output = [0] * len(arr)
    for num in reversed(arr):
        count[num] -= 1
        output[count[num]] = num

    return output


# Example
arr1 = [0, 2, 1, 3]
print("Sorted (non-negative only):", counting_sort_non_negative(arr1))



def counting_sort_with_negatives(arr):
    min_val = min(arr)
    max_val = max(arr)

    range_val = max_val - min_val + 1

    count = [0] * range_val

    # Step 4: Count frequencies (shifted by min_val)
    for num in arr:
        count[num - min_val] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    output = [0] * len(arr)
    for num in reversed(arr):
        count[num - min_val] -= 1
        output[count[num - min_val]] = num

    return output


# Example
arr2 = [-5, -2, 0, 3]
print("Sorted (with negatives):", counting_sort_with_negatives(arr2))
