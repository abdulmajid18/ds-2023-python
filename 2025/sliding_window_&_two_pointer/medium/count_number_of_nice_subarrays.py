from typing import List


def numberOfSubarraysBruteFOrce(nums: List[int], k: int) -> int:
    n = len(nums)
    res = 0
    for i in range(n):
        count_odd = 0
        for j in range(i, n):
            if nums[j] % 2 == 1:
                count_odd += 1
            if count_odd == k:
                res += 1
            elif count_odd > k:
                break
    return res


from collections import defaultdict

from collections import defaultdict
from typing import List


def numberOfSubarraysHAshMap(nums: List[int], k: int) -> int:
    count = defaultdict(int)
    count[0] = 1  # there's one way to have a prefix sum of 0 (by taking no elements)
    prefix_sum = 0
    res = 0

    for num in nums:
        # Increase prefix sum if the number is odd.
        if num % 2 == 1:
            prefix_sum += 1
        # If there's a prefix with (current prefix - k), those subarrays have exactly k odds.
        res += count[prefix_sum - k]
        # Record the current prefix sum.
        count[prefix_sum] += 1

    return res


def numberOfSubarraySlidingWindow(nums: List[int], k: int) -> int:

    def atMost(k):
        left = 0
        count = 0
        current_odds = 0

        for right, num in enumerate(nums):
            if num % 2 == 1:
                current_odds += 1

            while current_odds > k:
                num = nums[left]
                if num % 2 == 1:
                    current_odds -= 1
                left += 1

            count += right - left + 1
        return count

    return atMost(k) - atMost(k - 1)
