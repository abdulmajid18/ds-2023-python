class Solution:
    def sortArray(self, nums):
        def quicksort(left, right):
            if left < right:
                pivot_index = partition(left, right)
                quicksort(left, pivot_index - 1)
                quicksort(pivot_index + 1, right)

        def partition(left, right):
            pivot = nums[right]
            i = left
            for j in range(left, right):
                if nums[j] < pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[right] = nums[right], nums[i]
            return i

        quicksort(0, len(nums) - 1)
        return nums

