
def lower_bound(arr, x):
    """
    Finds the first (smallest) index in a sorted array where the value at that index is greater than or equal to x.

    Thought Process:
    1. Since the array is sorted, we iterate through it starting from the beginning.
    2. During the iteration, we check if the current element is greater than or equal to x.
    3. The first index that satisfies this condition is our answer.
    4. If no such index is found (all elements are smaller than x), return the size of the array.

    Time Complexity:
    - O(n) in the worst case, as we may need to traverse the entire array.

    Space Complexity:
    - O(1), since no extra space is used apart from variables.

    Parameters:
    - arr (List[int]): A sorted list of integers.
    - x (int): The target value.

    Returns:
    - int: The index of the lower bound of x in arr.
    """
    n = len(arr)
    for i in range(n):
        if arr[i] >= x:
            return i
    return n  # If no such index is found, return the size of the array.

# Example Usage
arr = [1, 2, 4, 6, 8, 10]
x = 5
print("Lower Bound index:", lower_bound(arr, x))


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
