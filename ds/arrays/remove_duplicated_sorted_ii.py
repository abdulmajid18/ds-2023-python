from typing import List


def remove_duplicates(nums: List[int]) -> int:
    if len(nums) <= 2:
        return len(nums)

    # Initialize two pointers
    i, j = 2, 2

    # Iterate through the array
    while j < len(nums):
        # If the current element is different from the element two positions back
        if nums[j] != nums[i - 2]:
            # Update the i-th element with the j-th element
            nums[i] = nums[j]
            # Move the i pointer forward
            i += 1
        # Move the j pointer forward
        j += 1

    # The length of the modified array is i
    return i


# Example usage:
nums = [1, 1, 1, 2, 2, 3]
result_length = remove_duplicates(nums)
print("Modified Array:", nums[:result_length])
