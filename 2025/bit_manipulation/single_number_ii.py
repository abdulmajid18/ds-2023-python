from typing import List


class Solution:
    def singleNumberBruteForce(self, nums: List[int]) -> int:
        nums.sort()  # Step 1: Sort the array

        # Step 2: Traverse in steps of 3
        for i in range(0, len(nums) - 1, 3):
            if nums[i] != nums[i + 1]:  # Unique number found
                return nums[i]

        # Step 3: Unique number is at the last index
        return nums[-1]  # If no mismatch was found earlier


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bits = [0] * 32

        for num in nums:
            for i in range(32):
                bits[i] += (num >> i) & 1

        result = 0
        for i in range(32):
            if bits[i] % 3:
                result |= (1 << i)

        if result >= (1 << 31):
            result -= (1 << 32)

        return result


from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count1, count2 = 0, 0  # Tracks bits appearing once and twice

        for num in nums:
            count1 = (count1 ^ num) & ~count2  # Update count1 while ensuring count2 bits are cleared
            count2 = (count2 ^ num) & ~count1  # Update count2 while ensuring count1 bits are cleared

        return count1  # Since count1 holds the unique number
