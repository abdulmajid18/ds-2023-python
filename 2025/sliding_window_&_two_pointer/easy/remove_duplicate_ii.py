class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0  # slow pointer

        for r in range(len(nums)):  # start fast pointer from index 1
            if nums[l] != nums[r]:  # found a unique element
                l += 1  # increment the slow pointer
                nums[l] = nums[r]  # move unique element to the left

        return l + 1  # return
