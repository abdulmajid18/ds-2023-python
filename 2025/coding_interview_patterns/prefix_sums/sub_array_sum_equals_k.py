from typing import List


def subarraySumBruteForce(nums: List[int], k: int) -> int:
    count = 0
    n = len(nums)
    for i in range(n):
        for j in range(i, n):
            cur_sum = 0
            for s in range(i, j + 1):
                cur_sum += nums[s]
            if cur_sum == k:
                count += 1
    return count


from typing import List


def subarraySumTwo(nums: List[int], k: int) -> int:
    n = len(nums)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]

    count = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            if prefix_sum[j] - prefix_sum[i] == k:
                count += 1
    return count


def subarraySumThree(nums: List[int], k: int) -> int:
    count = 0
    n = len(nums)
    prefix_sum = [0]

    for i in range(0, n):
        prefix_sum.append(prefix_sum[-1] + nums[i])

    for j in range(1, n + 1):
        for i in range(1, j + 1):
            if prefix_sum[j] - prefix_sum[i - 1] == k:
                count += 1
    return count


