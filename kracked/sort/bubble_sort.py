
nums = [3,2,1,4]

def bubble_sort(nums):
    n = len(nums)
    for j in range(n):
        for i in range(n-1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
    return nums

a =  bubble_sort(nums)
print(a)

def bubble_sort_optimized(nums):
    n = len(nums)
    for i in range(n):
        for j in range(n - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

nums = [3,2,1,4]
a =  bubble_sort_optimized(nums)
print(a)


def count_swaps(nums):
    count = 0
    n = len(nums)
    for i in range(n):
        for j in range(n - 1 - i):
            if nums[j] > nums[j + 1]:
                count += 1
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return count

nums = [3,2,1,4]
a =  count_swaps(nums)
print(a)