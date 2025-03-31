from typing import List


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


class SolutionBruteForce:
    def sortColors(self, nums: List[int]) -> None:
        count = [0, 0, 0]  # Store counts of 0s, 1s, and 2s

        # Count occurrences of each number
        for num in nums:
            count[num] += 1

        # Overwrite the array step by step
        index = 0
        for i in range(3):  # Iterate through [0, 1, 2]
            for _ in range(count[i]):
                nums[index] = i
                index += 1


# Example Usage
nums = [2, 0, 2, 1, 1, 0]
sol = SolutionBruteForce()
sol.sortColors(nums)
print(nums)  # Output: [0, 0, 1, 1, 2, 2]


def sortColors(nums):
    left, mid, right = 0, 0, len(nums) - 1

    while mid <= right:
        if nums[mid] == 0:
            nums[left], nums[mid] = nums[mid], nums[left]
            left += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[right] = nums[right], nums[mid]
            right -= 1