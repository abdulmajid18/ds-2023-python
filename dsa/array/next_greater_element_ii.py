from typing import List


def nextGreaterElements(nums: List[int]) -> List[int]:
    n = len(nums)
    res = [-1] * n  # Initialize result array with -1 for no greater elements
    stack = []  # Monotonic decreasing stack to store indices

    # Traverse the array twice to simulate circular behavior
    for i in range(2 * n):
        cur = nums[i % n]  # Get the current element (with wrapping via modulo)

        # While the stack is not empty and the current element is greater than
        # the element at the index on top of the stack, update the result
        while stack and nums[stack[-1]] < cur:
            res[stack.pop()] = cur

        # Only push the index in the first pass (i < n)
        if i < n:
            stack.append(i)

    return res
