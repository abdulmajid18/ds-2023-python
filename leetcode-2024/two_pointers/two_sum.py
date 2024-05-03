from typing import List


def two_sum_1(elements: List, target: int):
    for i in range(len(elements)):
        for j in range(len(elements)):
            if i == j:
                continue
            if elements[i] + elements[j] == target:
                return i + 1, j + 1


def two_brute_force(elements: list, target: int):
    for i in range(len(elements)):
        for j in range(len(elements)):
            if i == j:
                continue
            number = abs(target - elements[i])
            if elements[j] == number:
                return [i + 1, j + 1]


def two_sum_hashtable(self, elements: list, target: int):
    hash_map = {}
    for index, value in enumerate(elements):
        cache_number = target - value
        if cache_number in hash_map:
            return [hash_map[cache_number] + 1, index + 1]
        else:
            hash_map[value] = index
    return None


def twoSum3(nums, target):
    """ Not input should be sorted"""
    l, r = 0, len(nums) - 1
    while l < r:
        current_sum = nums[l] + nums[r]
        if current_sum == target:
            return [l + 1, r + 1]
        elif current_sum < target:
            l += 1
        else:
            r -= 1


def two_sum(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
    return None


if __name__ == '__main__':
    x = [1, 2, 3]
    target = 5

    result = two_sum_1(x, target)
    print(result)
    result_ = two_brute_force(x, target)
    print(result_)
