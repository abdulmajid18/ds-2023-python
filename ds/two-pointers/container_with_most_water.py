def maxAreaBrute(height):
    res = 0
    for l in range(len(height)):
        for r in range(l + 1, len(height)):
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)
    return res


def maxAreaOptimized(heights):
    res = 0
    l, r = 0, len(heights) - 1

    while l < r:
        area = (r - l) * min(heights[r], heights[l])
        res = max(res, area)

        if heights[r] > heights[l]:
            l += 1
        else:
            r -= 1

    return res
