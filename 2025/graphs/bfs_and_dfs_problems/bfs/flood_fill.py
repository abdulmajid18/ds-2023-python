from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        #  check if s is colored return image
        original_color = image[sr][sc]

        if original_color == color:
            return image

        rows, cols = len(image), len(image[0])

        #  perform bfs
        def bfs(r, c):
            from collections import deque
            queue = deque([(r, c)])

            while queue:
                r, c = queue.popleft()
                image[r][c] = color
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if (nr in range(rows) and nc in range(cols)) and image[nr][nc] == original_color:
                        queue.append((nr, nc))

        bfs(sr, sc)
        return image



