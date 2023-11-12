def sortColors(nums):
    l, r = 0, len(nums) - 1
    i = 0

    def swap(i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    while i <= r:
        if nums[i] == 0:
            swap(l, i)
            l += 1

        elif nums[i] == 2:
            swap(i, r)
            r -= 1
            i -= 1
        i += 1
    return nums


def sortColorsThreeWayPartition(nums):
    left, mid, right = 0, 0, len(nums) - 1

    while mid <= right:
        if nums[mid] == 0:
            nums[left], nums[mid] = nums[mid], nums[left]
            left += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[right] = nums[right], nums[mid]
            right -= 1

# Example usage:
nums = [2, 0, 2, 1, 1, 0]
sortColors(nums)
print(nums)  # This will print [0, 0, 1, 1, 2, 2]
