from typing import List
import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(l, r, pivot_index):
            pivot_val = nums[pivot_index]
            # Move pivot to end
            nums[pivot_index], nums[r] = nums[r], nums[pivot_index]
            store_index = l

            # Move smaller elements left
            for i in range(l, r):
                if nums[i] < pivot_val:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1

            # Move pivot to its final place
            nums[r], nums[store_index] = nums[store_index], nums[r]
            return store_index

        # K-th largest is (n-k)-th smallest
        target = len(nums) - k
        l, r = 0, len(nums) - 1

        while l <= r:
            pivot_index = random.randint(l, r)
            index = partition(l, r, pivot_index)
            if index == target:
                return nums[index]
            elif index < target:
                l = index + 1
            else:
                r = index - 1
        return None
