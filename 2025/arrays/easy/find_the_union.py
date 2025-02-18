# Function to find the union of two sorted arrays
def union_of_arrays_brute(a, b):
    # Convert both arrays to sets to remove duplicates and take the union
    union_set = set(a).union(set(b))

    # Convert the union set to a sorted list and return it
    return sorted(list(union_set))


# Example usage:
a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 6, 7]

# result = union_of_arrays_brute(a, b)
# print("Union of arrays:", result)

# Output: Union of arrays: [1, 2, 3, 4, 5, 6, 7]


# Function to find the union of two sorted arrays
def union_of_arrays(a, b):
    # Step 1: Create an empty set
    result_set = set()

    # Step 2: Add elements from both arrays to the set (duplicate elements will be ignored)
    for num in a:
        result_set.add(num)

    for num in b:
        result_set.add(num)

    # Step 3: Convert the set to a list and sort it
    result = list(result_set)
    result.sort()

    return result


# Example usage:
a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 6, 7]

# result = union_of_arrays(a, b)
# print("Union of arrays:", result)

# Output: Union of arrays: [1, 2, 3, 4, 5, 6, 7]

from collections import Counter


def union_of_sorted_arrays(arr1, arr2):
    """
    Find the union of two sorted arrays using a map (Counter in Python).
    The union should contain distinct elements, and the result should be sorted.

    Approach:
    - We use a map (or dictionary) to count the occurrences of each element in both arrays.
    - As we are using only one map, the common elements between the arrays are counted once.
    - By iterating over the keys of the map, we get the union in ascending order without needing extra sorting.

    Time Complexity: O(n + m), where n and m are the lengths of arr1 and arr2 (since we're traversing both arrays once).
    Space Complexity: O(n + m)(log(n+m)) for storing the elements in the map (or dictionary).
    """

    # Initialize an empty Counter to store frequencies
    freq_map = Counter()

    # Add elements from arr1
    for num in arr1:
        freq_map[num] += 1

    # Add elements from arr2
    for num in arr2:
        freq_map[num] += 1


    # Extract the sorted keys of the map as the union
    result = sorted(freq_map.keys())


    return result


# Example usage:
arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 3, 6, 7]

result = union_of_sorted_arrays(arr1, arr2)
print("Union of arrays:", result)

# Output: Union of arrays: [1, 2, 3, 4, 5, 6, 7]

