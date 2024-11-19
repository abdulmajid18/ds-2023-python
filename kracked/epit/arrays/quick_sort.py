def quick_sort(nums, start, end):
    # Base case: If the start index is greater than or equal to the end index, return
    if start >= end:
        return

    # Partition the array and get the pivot index
    p_index = partition(nums, start, end)

    # Recursively apply quick sort to the left and right subarrays
    quick_sort(nums, start, p_index - 1)  # Left subarray
    quick_sort(nums, p_index + 1, end)  # Right subarray


def partition(nums, start, end):
    # Select the pivot element (last element in this case)
    pivot = nums[end]

    # Initialize the partition index
    p_index = start

    # Rearrange elements around the pivot
    for i in range(start, end):
        if nums[i] < pivot:  # If current element is less than pivot
            nums[i], nums[p_index] = nums[p_index], nums[i]  # Swap
            p_index += 1

    # Swap the pivot element with the element at the partition index
    nums[p_index], nums[end] = nums[end], nums[p_index]

    return p_index  # Return the partition index


# Example usage:
nums = [10, 7, 8, 9, 1, 5]
quick_sort(nums, 0, len(nums) - 1)
print("Sorted array:", nums)
