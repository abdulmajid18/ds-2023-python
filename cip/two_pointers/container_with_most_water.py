from typing import List


def maxAreaBruteForce(height: List[int]) -> int:

    n = len(height)
    max_area = 0

    for i in range(n):
        left_height = height[i]
        for j in range(i + 1, n):
            right_height = height[j]
            area = (j - i) * min(left_height, right_height)
            max_area = max(max_area, area)

    return max_area


from typing import List


def maxAreaOptimized(height: List[int]) -> int:
    left = 0
    right = len(height) - 1
    max_area = 0

    while left < right:
        width = right - left
        current_area = width * min(height[left], height[right])
        max_area = max(max_area, current_area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area


from typing import List


def largest_container(heights: List[int]) -> int:
    max_water = 0
    left, right = 0, len(heights) - 1

    while left < right:
        water = min(heights[left], heights[right]) * (right - left)
        max_water = max(max_water, water)

        if heights[left] < heights[right]:
            left += 1
        elif heights[left] > heights[right]:
            right -= 1
        else:
            left += 1
            right -= 1

    return max_water
