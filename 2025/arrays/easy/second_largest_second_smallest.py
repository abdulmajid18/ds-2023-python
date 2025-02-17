import heapq


def find_second_largest_and_smallest(n, a):
    # Max heap for second largest
    max_heap = [-x for x in a]  # Negate the numbers to simulate max heap
    heapq.heapify(max_heap)

    # Pop the largest element (most negative in the max heap)
    largest = -heapq.heappop(max_heap)

    # Pop the second-largest element
    second_largest = -heapq.heappop(max_heap)

    # Min heap for second smallest
    min_heap = a[:]
    heapq.heapify(min_heap)

    # Pop the smallest element
    smallest = heapq.heappop(min_heap)

    # Pop the second smallest element
    second_smallest = heapq.heappop(min_heap)

    return [second_largest, second_smallest]


# Example Test Case
n = 5
a = [1, 2, 3, 4, 5]
result = find_second_largest_and_smallest(n, a)
print(result)  # Output: [4, 2]


def find_second_largest_and_smallest_sort(n, a):
    # Sort the array in ascending order
    a.sort()

    # The second-smallest element will be at index 1
    second_smallest = a[1]

    # The second-largest element will be at index n-2
    second_largest = a[-2]

    return [second_largest, second_smallest]


# Example Test Case
n = 5
a = [1, 2, 3, 4, 5]
result = find_second_largest_and_smallest(n, a)
print(result)  # Output: [4, 2]


def find_second_largest_and_smallest(n, a):
    """
    Find the second largest and second-smallest element from an array of unique non-negative integers.

    Approach:
    - First, we traverse the array to find the smallest and largest elements.
    - Then, we traverse the array again to find the second smallest (just greater than the smallest)
      and second largest (just smaller than the largest) elements.
    - This approach avoids sorting the array and ensures an O(n) time complexity.

    Time Complexity:
    - O(n), where n is the size of the input array.
    - We perform two full traversals of the array.

    Space Complexity:
    - O(1), as we only use a constant amount of extra space to track the smallest, largest,
      second smallest, and second largest elements.

    Arguments:
    n : int : The size of the input array.
    a : List[int] : The array of unique non-negative integers.

    Returns:
    List[int] : A list containing the second largest and second smallest elements.

    Example:
    >>> find_second_largest_and_smallest(5, [1, 2, 3, 4, 5])
    [4, 2]
    """

    if n < 2:
        return []

    # Initialize the smallest and largest
    smallest = float('inf')
    largest = -float('inf')

    # First traversal: find the smallest and largest elements
    for num in a:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num

    # Initialize second smallest and second largest
    second_smallest = float('inf')
    second_largest = -float('inf')

    # Second traversal: find the second smallest and second largest
    for num in a:
        if num > smallest and num < second_smallest:
            second_smallest = num
        if num < largest and num > second_largest:
            second_largest = num

    return [second_largest, second_smallest]


# Example Test Case
n = 5
a = [1, 2, 3, 4, 5]
result = find_second_largest_and_smallest(n, a)
print(result)  # Output: [4, 2]
