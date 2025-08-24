from typing import List


def merge_sort(nums: List[int]):
    n = len(nums)

    if n < 2:
        return
    m = n // 2
    left = nums[:m]
    right = nums[m:]

    merge_sort(left)
    merge_sort(right)

    k = i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        nums[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        nums[k] = right[j]
        j += 1
        k += 1

nums = [3, 1, 4, 2, 5]
merge_sort(nums)
print(nums)