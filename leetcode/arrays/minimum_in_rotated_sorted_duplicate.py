def minimum_rotated_1(elements):
    l = 0
    r = len(elements)

    while l < r and elements[l] >= elements[r]:
        m = (l + r) // 2
        if elements[m] > elements[r]:
            l = m + 1
        elif elements[m] < elements[l]:
            r = m
        else:
            l = l + 1
    return elements[l]


def findMin(nums):
    i = 0
    j = len(nums) - 1

    while i <= j:

        # Handle cases like [3, 1, 3]
        while nums[i] == nums[j] and i != j:
            i += 1

        if nums[i] <= nums[j]:
            return nums[i]

        m = (i + j) // 2
        if nums[m] >= nums[i]:
            i = m + 1
        else:
            j = m

    return -1
