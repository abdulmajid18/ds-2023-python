def bsearch(elements, target, begin):
    i = begin
    j = len(elements) - 1

    while i < j:
        mid = (i + j) // 2
        if elements[mid] < target:
            i = mid + 1
        else:
            j = mid

    if i == j and elements[j] == target:
        return j
    else:
        return -1




def two_sum_bsearch_two(elements, target):
    for i in range(len(elements)):
        index_2 = bsearch(elements, target - elements[i], i + 1)
        if index_2 != -1:
            return [i + 1, index_2 + 1]
    return None

def two_sum_bsearch(self, elements, target):
    left = 0
    right = len(elements) - 1

    while left < right:
        sum = elements[left] + elements[right]
        if sum > target:
            right -= 1
        elif sum < target:
            left += 1
        else:
            return [left+1, right+1]

if __name__ == '__main__':
    nums = sorted([2, 7, 11, 15])
    ans = two_sum_bsearch_two(nums, 9)
    print(ans)
