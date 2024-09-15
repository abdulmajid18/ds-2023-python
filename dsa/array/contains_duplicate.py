def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


def containsDuplicateOptimized(nums):
    nums.sort()  # O(n log n)
    for i in range(1, len(nums)):  # O(n)
        if nums[i] == nums[i - 1]:
            return True
    return False


def containsDuplicateBruteForce(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    return False


def containsDuplicateHashMap(nums):
    num_map = {}
    for num in nums:
        if num in num_map:
            return True
        num_map[num] = 1
    return False
