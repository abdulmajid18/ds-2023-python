def findMaxConsecutiveOnes(nums):
    l, res = 0, 0

    for r, n in enumerate(nums):
        if n == 0:
            l = r + 1
        res = max(res, r - l +1)
    return res