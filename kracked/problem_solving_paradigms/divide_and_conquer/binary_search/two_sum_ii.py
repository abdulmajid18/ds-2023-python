from typing import List, Any


def twoSum(self, numbers: List[int], target: int) -> list[int | Any] | None:
    l = 0
    r = len(numbers) - 1

    while l < r:
        mid = (l - r) // 2

        if numbers[l] + numbers[r] == target:
            return [l + 1, r + 1]
        elif numbers[l] + numbers[r] < target:
            l += 1
        else:
            r -= 1
    return None

from typing import List
import bisect

def twoSumBinarySearchOne(self, numbers: List[int], target: int) -> List[int]:
    n = len(numbers)

    for i in range(n):
        complement = target - numbers[i]
        # binary search in the right half
        j = bisect.bisect_left(numbers, complement, i + 1, n)

        if j < n and numbers[j] == complement:
            return [i + 1, j + 1]  # 1-based index

from typing import List

def twoSumBinarySearchThree(self, numbers: List[int], target: int) -> List[int]:
    n = len(numbers)

    def binary_search(left: int, right: int, target: int) -> int:
        while left <= right:
            mid = (left + right) // 2
            if numbers[mid] == target:
                return mid
            elif numbers[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    for i in range(n):
        complement = target - numbers[i]
        j = binary_search(i + 1, n - 1, complement)
        if j != -1:
            return [i + 1, j + 1]
    return None
