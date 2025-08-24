arr = [7, 10, 4, 3, 20, 15]
k = 3


def kth_smallest_naive(arr, k):
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



arr = [7, 10, 4, 3, 20, 15]
k = 3
print("The {}th smallest element is: {}".format(k, kth_smallest_naive(arr, k)))

