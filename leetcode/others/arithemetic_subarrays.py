from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def is_arithmetic(subarray):
            # Check if the subarray is an arithmetic sequence
            subarray.sort()
            diff = subarray[1] - subarray[0]
            for i in range(1, len(subarray)):
                if subarray[i] - subarray[i - 1] != diff:
                    return False
            return True

        result = []
        for i in range(len(l)):
            left, right = l[i], r[i] + 1  # Inclusive range
            subarray = nums[left:right]
            if is_arithmetic(subarray):
                result.append(True)
            else:
                result.append(False)

        return result