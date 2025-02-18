def rotate_one(nums, k):
    k %= len(nums)  # Handle cases where k > len(nums)
    nums[:] = nums[-k:] + nums[:-k]  # Slice and concatenate


# Example Usage:
nums1 = [1, 2, 3, 4, 5, 6, 7]
k1 = 3
rotate_one(nums1, k1)
print(nums1)  # Output: [5,6,7,1,2,3,4]

nums2 = [-1, -100, 3, 99]
k2 = 2
rotate_one(nums2, k2)
print(nums2)  # Output: [3,99,-1,-100]


def rotate(nums, k):
    n = len(nums)
    k %= n  # Handle cases where k is greater than the array length
    rotated = [0] * n  # Create a new array of the same length

    for i in range(n):
        rotated[(i + k) % n] = nums[i]  # Place elements in rotated positions

    nums[:] = rotated  # Update the original array to be the rotated one
