from typing import List


def maxAreaBrute(self, height: List[int]) -> int:
    n = len(height)
    area = 0
    for i in range(n):
        for j in range(i + 1, n):
            h = min(height[i], height[j])
            current_area = h * (j - i)
            area = max(area, current_area)
    return area

def maxArea(self, height: List[int]) -> int:
    res = 0
    n = len(height)
    l = 0
    r = n - 1

    while l < r:
        area = (r - l) * min(height[l], height[r])
        res = max(res, area)

        if height[l] < height[r]:
            l += 1
        elif height[l] > height[r]:
            r -= 1
        else:
            r -= 1
        return res