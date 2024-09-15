def containsNearbyDuplicate(nums, k):
    num_map = {}
    for i, num in enumerate(nums):
        if num in num_map and i - num_map[num] <= k:
            return True
        num_map[num] = i
    return False


def containsNearbyDuplicateSlidingWindow(nums, k):
    window = set()
    L = 0

    for R in range(len(nums)):
        if R - L > k:
            window.remove(nums[L])
            L += 1
        if nums[R] in window:
            return True
        window.add(nums[R])
    return False


def containsNearbyDuplicateSliding2(nums, k):
    window = set()

    for i in range(len(nums)):
        if nums[i] in window:
            return True

        window.add(nums[i])

        if len(window) > k:
            window.remove(nums[i - k])

    return False
