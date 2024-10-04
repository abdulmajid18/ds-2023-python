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
