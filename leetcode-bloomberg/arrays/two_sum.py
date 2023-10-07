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


# Prompt: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
def twoSum(self, nums: List[int], target: int) -> List[int]:
    nums_dict = {val: idx for idx, val in enumerate(nums)}
    for idx, val in enumerate(nums):
        looking_for = target - val
        if looking_for in nums_dict and nums_dict[looking_for] != idx:
            return [idx, nums_dict[looking_for]]


if __name__ == '__main__':
    x = [1, 2, 3]
    target = 5

    result = two_sum_1(x, target)
    print(result)
    result_ = two_brute_force(x, target)
    print(result_)
