from typing import List


class SolutionBruteForce:
    def findPairs(self, nums: List[int], k: int) -> int:

        res = set()
        for i in range(len(nums)):
            for j in range(i + 1,len(nums)):
                if abs(nums[i]-nums[j]) == k:
                    res.add((min(nums[i], nums[j]), max(nums[i], nums[j])))
        return len(res)


from typing import List
from collections import Counter


class SolutionOptiml1:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0  # Absolute difference cannot be negative

        freq = Counter(nums)  # Count occurrences of each number
        count = 0

        for num in freq:
            if k == 0:
                # If k == 0, count elements that appear at least twice
                if freq[num] > 1:
                    count += 1
            else:
                # If k > 0, check if num + k exists in hashmap
                if num + k in freq:
                    count += 1

        return count


from typing import List

class SolutionTwoPointers:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0  # Since absolute difference cannot be negative

        nums.sort()  # Sorting helps us efficiently find pairs
        left, right = 0, 1  # Two pointers
        count = 0
        n = len(nums)

        while left < n and right < n:
            # Avoid checking the same element against itself
            if left == right or nums[right] - nums[left] < k:
                right += 1  # Expand the window to increase the difference
            elif nums[right] - nums[left] > k:
                left += 1  # Move left pointer to reduce the difference
            else:  # nums[right] - nums[left] == k (Valid pair found)
                count += 1
                left += 1  # Move left pointer to the next unique number

                # Skip duplicates for `left`
                while left < n and nums[left] == nums[left - 1]:
                    left += 1

        return count
