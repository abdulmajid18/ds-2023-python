from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        original_color = image[sr][sc]

        # If the original color is the same as the new color, return early
        if original_color == color:
            return image

        # Perform DFS
        def dfs(r, c):
            # Base condition: Out of bounds or different color
            if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != original_color:
                return

            # Fill the current cell
            image[r][c] = color

            # Explore the four directions (up, down, left, right)
            dfs(r - 1, c)  # Up
            dfs(r + 1, c)  # Down
            dfs(r, c - 1)  # Left
            dfs(r, c + 1)  # Right

        dfs(sr, sc)
        return image
