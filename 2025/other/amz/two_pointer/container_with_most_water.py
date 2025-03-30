class Solution:
    def maxAreaBruteForce(self, height: list[int]) -> int:
        max_area = 0
        n = len(height)

        for left in range(n):
            for right in range(left + 1, n):
                area = (right - left) * min(height[left], height[right])
                max_area = max(max_area, area)

        return max_area


class SolutionOptimal:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            area = (right - left) * min(height[left], height[right])
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
