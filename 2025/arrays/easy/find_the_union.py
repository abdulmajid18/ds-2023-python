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

def union_of_sorted_arrays_optimal(arr1, arr2):
    """
    Find the union of two sorted arrays in O(n + m) time without sorting.
    The union should contain distinct elements, and the result should be sorted.

    Approach:
    - Use two pointers to traverse both arrays.
    - If the elements pointed to by both pointers are the same, add the element to the result and move both pointers.
    - If one element is smaller, move the pointer for that array.
    - Continue until both arrays are fully traversed.

    Time Complexity: O(n + m)
    Space Complexity: O(n + m) for the result array.
    """
    i, j = 0, 0  # Initialize pointers for arr1 and arr2
    union = []  # Vector to store the union

    # Traverse both arrays simultaneously
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            # If both elements are equal, add only one and move both pointers
            if not union or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            # If arr1[i] is smaller, add arr1[i] and move pointer i
            if not union or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1
        else:
            # If arr1[i] is larger, add arr2[j] and move pointer j
            if not union or union[-1] != arr2[j]:
                union.append(arr2[j])
            j += 1

    # Add remaining elements from arr1
    while i < len(arr1):
        if not union or union[-1] != arr1[i]:
            union.append(arr1[i])
        i += 1

    # Add remaining elements from arr2
    while j < len(arr2):
        if not union or union[-1] != arr2[j]:
            union.append(arr2[j])
        j += 1

    return union


# Example usage:
arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 3, 6, 7]

result = union_of_sorted_arrays(arr1, arr2)
print("Union of arrays:", result)

# Output: Union of arrays: [1, 2, 3, 4, 5, 6, 7]
