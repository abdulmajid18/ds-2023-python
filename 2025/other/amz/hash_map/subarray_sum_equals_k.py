from typing import List


class SolutionBruteForceOne:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            current_sum = 0
            for j in range(i, len(nums)):
                current_sum += nums[j]
                if current_sum == k:
                    count += 1
        return count


from typing import List


class SolutionBruteTwo:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if sum(nums[i:j + 1]) == k:  # Compute subarray sum using slicing
                    count += 1
        return count


from typing import List


class SolutionBruteThreeEarlyTermination:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            current_sum = 0
            for j in range(i, len(nums)):
                current_sum += nums[j]
                if current_sum == k:
                    count += 1
                elif current_sum > k:
                    break
        return count


from typing import List


class SolutionOptimal:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        prefixSums = {0: 1}

        for n in nums:
            curSum += n
            diff = curSum - k

            res += prefixSums.get(diff, 0)
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)
        return res

    def subArraySumTwo(self, nums: List[int], k: int) -> int:
        total = 0
        dict = {}
        counter = 0

        for i in range(len(nums)):
            total += nums[i]

            if total == k:
                counter += 1

            if (total - k) in dict:
                counter += dict[total - k]

            if total in dict:
                dict[total] += 1
            else:
                dict[total] = 1

        return counter


from collections import defaultdict


class SolutionOptimalTwo:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_count = defaultdict(int)
        prefix_sum_count[0] = 1  # Default case when subarray starts from index 0

        prefix_sum = 0
        count = 0

        for num in nums:
            prefix_sum += num  # Compute running sum

            # Check if (prefix_sum - k) exists in the map
            if (prefix_sum - k) in prefix_sum_count:
                count += prefix_sum_count[prefix_sum - k]

            # Store the prefix_sum in the hashmap
            prefix_sum_count[prefix_sum] += 1

        return count


class SolutionPositiveIntegers:
    def longestSubarraySumAtMostK(self, nums: List[int], k: int) -> int:
        left = 0  # Left pointer
        current_sum = 0
        max_length = 0

        for right in range(len(nums)):
            current_sum += nums[right]  # Expand window

            # Shrink window if sum exceeds k
            while current_sum > k:
                current_sum -= nums[left]
                left += 1

            # Update max length
            max_length = max(max_length, right - left + 1)

        return max_length
