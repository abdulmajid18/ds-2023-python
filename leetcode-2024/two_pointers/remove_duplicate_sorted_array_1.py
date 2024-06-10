from typing import List

class Solution:
    def removeDuplicates(self, nums):
        i = 0
        j = 1

        while j < len(nums):
            if nums[j] == nums[j - 1]:
                j += 1
            else:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

        return i + 1


def remove_1(elements: List):
    result = set()
    for i in elements:
        result.add(i)
    print(result)
    return len(result)

def remove_4(elements):
    l = 1

    for r in range(1, len(elements)):
        if elements[r] != elements[r-1]:
            elements[l] = elements[r]
            l += 1

    return l + 1

def remove_2(elements: List):
    l = 1
    for i in range(1, len(elements)):
        if elements[i] != elements[i - 1]:
            elements[l] = elements[i]
            l += 1
    return l


def remove_3(elements: List):
    if len(elements) < 2:
        return len(elements)

    i = 0
    j = 1

    while j < len(elements):
        if elements[i] != elements[j]:
            i += 1
            elements[i] = elements[j]
        j += 1
    return j + 1






if __name__ == '__main__':
    x = [1, 1, 2]
    ans = remove_1(x)
    print(ans)
    ans_2 = remove_2(x)
    print(ans_2)
