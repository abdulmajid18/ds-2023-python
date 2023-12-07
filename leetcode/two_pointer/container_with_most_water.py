def max_area(heights):
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