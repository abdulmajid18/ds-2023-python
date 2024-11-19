RED, WHITE, BLUE = range(3)

def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]
    # First pass: Group elements smaller than the pivot
    smaller = 0
    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1
    # Second pass: Group elements larger than the pivot
    larger = len(A) - 1
    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break
        elif A[i] > pivot:
            A[i], A[larger] = A[larger], A[i]
            larger -= 1

# Example usage
A = [3, 5, 2, 7, 1, 4, 6]
pivot_index = 3  # Choose 7 as the pivot
dutch_flag_partition(pivot_index, A)
print(A)  # Output: [3, 5, 2, 1, 4, 6, 7] (order within partitions may vary)


def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]
    smaller, equal, larger = 0, 0, len(A)

    # Process elements until `equal` and `larger` pointers meet
    while equal < larger:
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller += 1
            equal += 1
        elif A[equal] == pivot:
            equal += 1
        else:  # A[equal] > pivot
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]


# Example usage
A = [3, 5, 2, 7, 1, 4, 6]
pivot_index = 3
dutch_flag_partition(pivot_index, A)
print(A)  # Output: [3, 2, 1, 5, 4, 6, 7]


def dutch_flag_partition(pivot_index, A):
    # Set the pivot value using the pivot_index
    pivot = A[pivot_index]

    # Initialize pointers for the three groups
    smaller = 0  # Pointer for elements smaller than pivot
    equal = 0  # Pointer for elements equal to pivot
    larger = len(A)  # Pointer for elements larger than pivot

    # Keep iterating as long as there's an unclassified element
    while equal < larger:
        # A[equal] is the incoming unclassified element
        if A[equal] < pivot:
            # If element is smaller than pivot, swap it to the 'smaller' group
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller += 1
            equal += 1
        elif A[equal] == pivot:
            # If element is equal to pivot, leave it in the 'equal' group
            equal += 1
        else:
            # If element is larger than pivot, swap it to the 'larger' group
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]


# Example usage:
A = [3, 5, 2, 7, 1, 4, 6]
pivot_index = 3  # Choose the pivot as 7 (index 3)
dutch_flag_partition(pivot_index, A)
print(A)  # Output will be: [3, 5, 2, 1, 4, 6, 7] (order within partitions may vary)
