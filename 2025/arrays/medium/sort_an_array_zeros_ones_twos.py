from typing import List


class Solution:
    def sortColors(nums):
        """
        This function sorts an array consisting of 0s, 1s, and 2s in-place using the Dutch National Flag algorithm.

        Thought Process:
        - We use three pointers: `left`, `mid`, and `right`.
        - `left` starts at index 0, `mid` starts at index 0, and `right` starts at the last index.
        - We traverse the array using `mid` and handle elements as follows:
          - If nums[mid] == 0, swap nums[left] and nums[mid], then increment both `left` and `mid`.
          - If nums[mid] == 1, just move `mid` forward as it is in the correct position.
          - If nums[mid] == 2, swap nums[mid] and nums[right], then decrement `right`.
        - The key observation is that `left` and `mid` start together, and `left` lags behind `mid` only when encountering 1s.
        - When swapping 0s, we ensure `left` moves forward, guaranteeing that elements before `left` are all 0s.
        - When swapping 2s, we ensure that elements after `right` are all 2s, without moving `mid` immediately since the swapped element at `mid` needs checking.

        Time Complexity: O(N) - Each element is processed at most once.
        Space Complexity: O(1) - Sorting is done in-place.

        Example:
        >>> nums = [2, 0, 2, 1, 1, 0]
        >>> sortColors(nums)
        >>> print(nums)
        [0, 0, 1, 1, 2, 2]
        """
        left, mid, right = 0, 0, len(nums) - 1

        while mid <= right:
            if nums[mid] == 0:
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1


def sortColors(nums):
    l, r = 0, len(nums) - 1
    i = 0

    def swap(i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

    while i <= r:
        if nums[i] == 0:
            swap(l, i)
            l += 1
            i += 1
            ...
        elif nums[i] == 2:
            swap(i, r)
            r -= 1
            i -= 1
        i += 1


def sortColorsQuickSort(nums):
    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1


# Example usage:
nums = [2, 0, 2, 1, 1, 0]
sortColors(nums)
print(nums)  # Output: [0, 0, 1, 1, 2, 2]


def sortColorsBucketSort(nums):
    count = [0] * 3  # For 0, 1, 2

    # Count the occurrences of each number
    for num in nums:
        count[num] += 1

    # Overwrite the array based on the counts
    index = 0
    for i in range(3):
        for _ in range(count[i]):
            nums[index] = i
            index += 1


# Example usage:
nums = [2, 0, 2, 1, 1, 0]
sortColors(nums)
print(nums)  # Output: [0, 0, 1, 1, 2, 2]
