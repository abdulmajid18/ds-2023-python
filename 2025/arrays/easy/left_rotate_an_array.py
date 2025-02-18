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


def rotate_optimal(nums, k):
    """
    Rotates the array `nums` to the right by `k` steps using the reversal algorithm.

    Steps:
    1. Reverse the entire array.
    2. Reverse the first `k` elements.
    3. Reverse the remaining elements.

    Time Complexity: O(n), where n is the length of the array.
    Space Complexity: O(1), as no additional space is used.

    Parameters:
    nums (List[int]): The input array to rotate.
    k (int): The number of steps to rotate the array to the right.
    """

    n = len(nums)

    # Handle the case where k is larger than the array length.
    k %= n  # Normalize k to avoid unnecessary rotations.

    # Step 1: Reverse the entire array.
    nums.reverse()

    # Step 2: Reverse the first k elements.
    nums[:k] = reversed(nums[:k])

    # Step 3: Reverse the remaining n-k elements.
    nums[k:] = reversed(nums[k:])


# Example Usage:
arr1 = [1, 2, 3, 4, 5, 6, 7]
k1 = 3
rotate(arr1, k1)
print(arr1)  # Output: [5, 6, 7, 1, 2, 3, 4]

arr2 = [-1, -100, 3, 99]
k2 = 2
rotate(arr2, k2)
print(arr2)  # Output: [3, 99, -1, -100]
