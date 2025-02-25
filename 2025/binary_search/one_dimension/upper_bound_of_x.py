def find_floor_and_ceil(arr, x):
    """
    Given an unsorted array arr of integers and an integer x, find the floor and ceiling of x.
    Floor of x is defined as the largest element in arr that is less than or equal to x.
    Ceiling of x is defined as the smallest element in arr that is greater than or equal to x.
    Return a list [floor, ceiling] where floor or ceiling is -1 if not present.

    Thought Process:
    1. Sort the array to enable binary search.
    2. Use binary search to find the lower bound index for x (the first index at which the element is >= x).
       - Initialize low = 0, high = n (size of array), and ans = n.
       - While low < high, compute mid = (low + high) // 2.
       - If arr[mid] is greater than or equal to x, update ans = mid and set high = mid.
       - Otherwise, set low = mid + 1.
    3. Determine the ceiling:
       - If ans equals n, no element in arr is >= x, so ceiling is -1.
       - Otherwise, ceiling is arr[ans].
    4. Determine the floor:
       - If ans is within bounds and arr[ans] equals x, then floor is arr[ans].
       - Else, if ans is 0, x is smaller than every element so floor is -1.
       - Otherwise, floor is arr[ans - 1] (the largest element that is < x).
    """
    arr.sort()
    n = len(arr)
    low, high, ans = 0, n, n
    while low < high:
        mid = (low + high) // 2
        if arr[mid] >= x:
            ans = mid
            high = mid
        else:
            low = mid + 1
    ceiling = -1 if ans == n else arr[ans]
    if ans < n and arr[ans] == x:
        floor_val = arr[ans]
    else:
        floor_val = -1 if ans == 0 else arr[ans - 1]
    return [floor_val, ceiling]


# Test cases:
# Test 1
x1 = 7
arr1 = [5, 6, 8, 9, 6, 5, 5, 6]
print(find_floor_and_ceil(arr1, x1))  # Expected Output: [6, 8]

# Test 2
x2 = 10
arr2 = [5, 6, 8, 8, 6, 5, 5, 6]
print(find_floor_and_ceil(arr2, x2))  # Expected Output: [8, -1]