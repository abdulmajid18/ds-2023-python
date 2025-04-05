from typing import List


def rotateBruteForce(nums: List[int], k: int) -> None:
    n = len(nums)
    k %= n  # handle cases where k > n

    for _ in range(1):
        prev = nums[-1]
        for i in range(n):
            nums[i], prev = prev, nums[i]


nums = [1, 2, 3, 4, 5, 6, 7]
rotateBruteForce(nums, 3)


# print(nums)
# [5, 6, 7, 1, 2, 3, 4]

def rotate(nums: List[int], k: int) -> None:
    n = len(nums)
    k %= n

    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    reverse(0, n - 1)  # Step 1: Reverse all
    reverse(0, k - 1)  # Step 2: Reverse first k
    reverse(k, n - 1)  # Step 3: Reverse remaining
