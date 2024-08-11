class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = -1
        for k in range(len(nums) - 2, -1, -1):
            if nums[k] < nums[k + 1]:
                i = k
                break

        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1

            nums[i], nums[j] = nums[j], nums[i]

        nums[i + 1:] = reversed(nums[i + 1:])