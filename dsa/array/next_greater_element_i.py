from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Idx = {n: i for i, n in enumerate(nums1)}
        res = [-1] * len(nums1)

        for i in range(len(nums2)):
            if nums2[i] not in nums1Idx:
                continue
            for j in range(i + 1, len(nums2)):
                if nums2[j] > nums2[i]:
                    idx = nums1Idx[nums2[i]]
                    res[idx] = nums2[j]
                    break
        return res


def nextGreaterElement(nums1, nums2):
    # Dictionary to map each number in nums2 to its next greater element
    next_greater = {}
    # Monotonic stack to keep track of decreasing elements
    stack = []

    # Traverse the nums2 array
    for num in nums2:
        # While stack is not empty and the current number is greater than the top of the stack
        while stack and num > stack[-1]:
            # Pop the top element of the stack and map it to the current number (which is its next greater element)
            next_greater[stack.pop()] = num
        # Push the current number onto the stack
        stack.append(num)

    # For any remaining elements in the stack, their next greater element doesn't exist, so map them to -1
    while stack:
        next_greater[stack.pop()] = -1

    # Use the dictionary to get the result for nums1
    result = [next_greater[num] for num in nums1]
    return result


# Example usage:
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(nextGreaterElement(nums1, nums2))  # Output: [-1, 3, -1]

from typing import List


def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    # Create a map of the index of elements in nums1 for easy lookup
    nums1Idx = {n: i for i, n in enumerate(nums1)}

    # Initialize the result list with -1 (default when no greater element is found)
    res = [-1] * len(nums1)

    # Monotonic stack to track the decreasing sequence in nums2
    stack = []

    # Iterate through nums2
    for cur in nums2:
        # While the stack is not empty and the current number is greater than the top of the stack
        while stack and cur > stack[-1]:
            # Pop the top element from the stack
            val = stack.pop()
            # Get the index of this element from nums1
            if val in nums1Idx:
                idx = nums1Idx[val]
                # Set the result for this index to the current number
                res[idx] = cur

        # If the current number is in nums1, push it onto the stack
        if cur in nums1Idx:
            stack.append(cur)

    return res
