"""
Given a sorted array, arr[] and a number target, you need to find the number of occurrences of target in arr[].
"""


def count_occurrences_bruteforce(arr, target):
    count = 0
    for num in arr:
        if num == target:
            count += 1
    return count


# Example usage
arr = [1, 1, 2, 2, 2, 2, 3]
target = 2
print(count_occurrences_bruteforce(arr, target))  # Output: 4

from collections import Counter


def count_occurrences_hashmap(arr, target):
    freq_map = Counter(arr)
    return freq_map.get(target, 0)


# Example usage
print(count_occurrences_hashmap(arr, target))  # Output: 4


def find_first_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    first = -1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            first = mid
            right = mid - 1  # Move left to find first occurrence
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return first


def find_last_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    last = -1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            last = mid
            left = mid + 1  # Move right to find last occurrence
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return last


def count_occurrences_binarysearch(arr, target):
    first = find_first_occurrence(arr, target)
    if first == -1:  # Target not found
        return 0
    last = find_last_occurrence(arr, target)
    return last - first + 1


# Example usage
arr = [1, 1, 2, 2, 2, 2, 3]
target = 2
print(count_occurrences_binarysearch(arr, target))  # Output: 4

target = 4
print(count_occurrences_binarysearch(arr, target))  # Output: 0
