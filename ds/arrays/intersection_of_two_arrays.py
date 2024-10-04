from typing import List


def intersection(nums1, nums2):
    set1 = set(nums1)  # Convert nums1 to set to eliminate duplicates
    result = set()     # Initialize an empty set to store the result

    for num in nums2:
        if num in set1:  # Check if num from nums2 exists in set1
            result.add(num)

    return list(result)


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_set = set(nums1)
        res = []
        for n in nums2:
            if n in nums1_set:
                res.append(n)
                nums1_set.remove(n)
        return res


def intersectionTwoPointers(nums1, nums2):
    # Sort both arrays
    nums1.sort()
    nums2.sort()

    i, j = 0, 0
    result = set()

    # Use two pointers to find common elements
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            result.add(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1

    return list(result)


def intersectionHashSet(nums1, nums2):
    # Create a hashmap from nums1
    count = {}
    for num in nums1:
        count[num] = 1

    result = set()

    # Find common elements by checking existence in the hashmap
    for num in nums2:
        if num in count:
            result.add(num)

    return list(result)
