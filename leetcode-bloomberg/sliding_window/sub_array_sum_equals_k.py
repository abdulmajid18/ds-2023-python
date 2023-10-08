from typing import List


def solution(nums, k):
    count = 0
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums) + 1):
            if j == 3:
                print(i, j)
            if sum(nums[i:j]) == k:
                count += 1
    return count


def subarraySum(nums: List[int], k: int) -> int:
    count = 0

    for i in range(0, len(nums)):
        current_sum = 0

        for j in range(i, len(nums)):
            print(i, j)
            current_sum += nums[j]

            if current_sum == k:
                count += 1

    return count


def subarraySumPrefixSum(self, nums: List[int], k: int) -> int:
    running = 0
    total = 0

    sum_frequency = {0: 1}

    for i in range(0, len(nums)):
        running += nums[i]
        target_sum = running - k

        if target_sum in sum_frequency:
            total += sum_frequency[target_sum]

        sum_frequency[running] = sum_frequency.get(running, 0) + 1

    return total


if __name__ == '__main__':
    nums = [3, 2, 1]
    k = 3
    ans = subarraySum(nums, k)
    print(ans)
