from typing import List


class SolutionBruteForceOne:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        repeating, missing = -1, -1

        for i in range(1, n + 1):  # Check every number from 1 to n
            count = nums.count(i)
            if count == 2:
                repeating = i
            elif count == 0:
                missing = i

        return [repeating, missing]


from collections import defaultdict
from typing import List


class SolutionBruteForceThree:
    def findErrorNums(self, arr: List[int]) -> List[int]:
        count = defaultdict(int)
        n = len(arr)
        repeating, missing = -1, -1

        # Count occurrences
        for num in arr:
            count[num] += 1

        # Find repeating and missing
        for i in range(1, n + 1):
            if count[i] == 2:
                repeating = i
            elif count[i] == 0:
                missing = i

        return [repeating, missing]


def findErrorNumsOptimal(arr: List[int]) -> List[int]:
    n = len(arr)
    xor_all = 0

    # XOR all numbers from 1 to n and array elements
    for num in arr:
        xor_all ^= num
    for i in range(1, n + 1):
        xor_all ^= i

    # Find rightmost set bit
    rightmost_bit = xor_all & -xor_all
    x = y = 0

    # Divide numbers into two sets
    for num in arr:
        if num & rightmost_bit:
            x ^= num
        else:
            y ^= num
    for i in range(1, n + 1):
        if i & rightmost_bit:
            x ^= i
        else:
            y ^= i

    # Identify missing and repeating
    if arr.count(x) == 2:
        return [x, y]
    return [y, x]

