
def find_kth_element(arr, k):
    n = len(arr)

    if k == 1:
        current_min = arr[0]
        for i in range(1, n):
            if arr[i] < current_min:
                current_min = arr[i]
        return current_min
    elif k == n:  # Find maximum
        answer = arr[0]
        for i in range(1, n):
            if arr[i] > answer:
                answer = arr[i]
        return answer
    return None

arr = [12, 5, 7, 3, 19, 1, 25]
n = len(arr)

print("Array:", arr)
print("Minimum element (k=1):", find_kth_element(arr, 1))
print("Maximum element (k=n):", find_kth_element(arr, n))