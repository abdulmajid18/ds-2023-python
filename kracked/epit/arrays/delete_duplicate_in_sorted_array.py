def remove_duplicate(nums):
    if not nums:
        return 0  # Return 0 for empty list

    l = 1
    for r in range(1, len(nums)):
        if nums[r] != nums[r - 1]:
            nums[l] = nums[r]
            l += 1

    return l


# Returns the number of valid entries after deletion
def delete_duplicates(A):
    if not A:
        return 0  # Return 0 for empty lists

    write_index = 1
    for i in range(1, len(A)):
        if A[write_index - 1] != A[i]:  # Check for duplicates
            A[write_index] = A[i]  # Write the non-duplicate value
            write_index += 1  # Move to the next write position

    return write_index  # Return the count of unique elements
