def findClosestElements(arr, k, x):
    left, right = 0, len(arr) - 1

    # Use binary search to find the closest element
    while right - left >= k:
        if abs(arr[left] - x) > abs(arr[right] - x):
            left += 1
        else:
            right -= 1

    return arr[left:right+1]
