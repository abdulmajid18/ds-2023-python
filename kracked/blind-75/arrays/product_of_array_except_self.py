from typing import List


class Solution:
    def productExceptSelfBrute(self, nums):
        n = len(nums)
        result = [1] * n  # Initialize result array with 1's

        for i in range(n):
            product = 1
            # Calculate product of all elements except nums[i]
            for j in range(n):
                if i != j:
                    product *= nums[j]
            result[i] = product

        return result


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Initialize prefix and postfix arrays
        prefix = [1] * n
        postfix = [1] * n

        # Compute prefix products
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        # Compute postfix products
        for i in range(n - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i + 1]

        # Multiply prefix and postfix to get the result
        result = [prefix[i] * postfix[i] for i in range(n)]

        return result


class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        result = [1] * n  # Initialize result array with 1's

        # Compute the prefix product
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]  # Update the prefix product for the next element

        # Compute the postfix product and update the result
        postfix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]  # Update the postfix product for the next element

        return result
