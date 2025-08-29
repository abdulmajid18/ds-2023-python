from typing import List


def findDuplicates(nums: List[int]) -> List[int]:
    res = []

    for n in nums:

        n = abs(n)

        if nums[n - 1] < 0:
            res.append(n)

        nums[n - 1] = -nums[n - 1]

    return res


from typing import List


def findDuplicatesTwo(nums: List[int]) -> List[int]:
    res = []
    for num in nums:
        index = abs(num) - 1
        if nums[index] < 0:
            res.append(abs(num))
        else:
            nums[index] = -nums[index]
    return res

