
def floor_search(arr, k):
    """
    Given a sorted array arr[] (with unique elements) and an integer k, find the index (0-based)
    of the largest element in arr[] that is less than or equal to k.
    This element is called the "floor" of k. If such an element does not exist, return -1.

    Thought process:
    - Initialize two pointers, low and high, to represent the current search space.
    - Use binary search: while the search space is valid, compute the middle index (mid).
    - If arr[mid] is less than or equal to k, record mid as a candidate (floor_index) and move low to mid + 1
      to search for a potentially larger candidate.
    - If arr[mid] is greater than k, move high to mid - 1 to restrict the search to the left half.
    - Continue until the search space is exhausted (low > high), at which point floor_index contains the result.
    """
    low, high = 0, len(arr) - 1
    floor_index = -1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= k:
            floor_index = mid
            low = mid + 1
        else:
            high = mid - 1

    return floor_index
