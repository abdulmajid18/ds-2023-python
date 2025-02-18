# Function to find the union of two sorted arrays
def union_of_arrays_brute(a, b):
    # Convert both arrays to sets to remove duplicates and take the union
    union_set = set(a).union(set(b))

    # Convert the union set to a sorted list and return it
    return sorted(list(union_set))


# Example usage:
a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 6, 7]

result = union_of_arrays_brute(a, b)
print("Union of arrays:", result)

# Output: Union of arrays: [1, 2, 3, 4, 5, 6, 7]
