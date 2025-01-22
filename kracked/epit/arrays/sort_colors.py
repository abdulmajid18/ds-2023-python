def sortColors(nums):
    l, r = 0, len(nums) - 1
    i = 0

    def swap(i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

    while i <= r:
        if nums[i] == 0:
            swap(l, i)
            l += 1
            i += 1
            ...
        elif nums[i] == 2:
            swap(i, r)
            r -= 1
            i -= 1
        i += 1


def sortColorsQuickSort(nums):
    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1


# Example usage:
nums = [2, 0, 2, 1, 1, 0]
sortColors(nums)
print(nums)  # Output: [0, 0, 1, 1, 2, 2]


def sortColorsBucketSort(nums):
    count = [0] * 3  # For 0, 1, 2

    # Count the occurrences of each number
    for num in nums:
        count[num] += 1

    # Overwrite the array based on the counts
    index = 0
    for i in range(3):
        for _ in range(count[i]):
            nums[index] = i
            index += 1


# Example usage:
nums = [2, 0, 2, 1, 1, 0]
sortColors(nums)
print(nums)  # Output: [0, 0, 1, 1, 2, 2]
