class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0

        # Cyclic sort
        while i < n:
            correct_idx = nums[i] - 1
            if nums[i] != nums[correct_idx]:
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            else:
                i += 1

        # Find duplicate + missing
        for i in range(n):
            if nums[i] != i + 1:
                return [nums[i], i + 1]
