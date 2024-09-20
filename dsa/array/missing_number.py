class Solution:
    def missingNumber(self, nums):
        # Convert nums into a set for O(1) lookup
        num_set = set(nums)

        # Check for the missing number by scanning from 0 to n
        for i in range(len(nums) + 1):
            if i not in num_set:
                return i


class Solution:
    def missingNumberOptimized(self, nums):
        n = len(nums)
        xor_result = 0

        # XOR all indices and nums together
        for i in range(n + 1):
            xor_result ^= i

        for num in nums:
            xor_result ^= num

        return xor_result
