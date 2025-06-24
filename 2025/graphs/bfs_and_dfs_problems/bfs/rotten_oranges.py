from typing import List


def orangesRotting(grid: List[List[int]]) -> int:
    from collections import deque

    q = deque()
    time, fresh = 0, 0

    ROWS, COLS = len(grid), len(grid[0])
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1:
                fresh += 1
            if grid[r][c] == 2:
                q.append([r, c])

    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    while q and fresh > 0:

        for i in range(len(q)):
            r, c = q.popleft()
            for dr, dc in directions:
                row, col = dr + r, dc + c
                if (row < 0 or row == len(grid) or
                    col < 0 or col == len(grid[0]) or
                    grid[row][col] != 1):
                    continue
                grid[row][col] = 2
                q.append([row, col])
                fresh -= 1
        time += 1

    return time if fresh == 0 else -1




from collections import deque

def orangesRottingTwo(grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh = 0

    # Step 1: Initialize queue with all rotten oranges
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c, 0))  # (row, col, time)
            elif grid[r][c] == 1:
                fresh += 1

    directions = [(0,1), (1,0), (-1,0), (0,-1)]
    time = 0

    # Step 2: BFS to rot adjacent oranges
    while queue:
        r, c, t = queue.popleft()
        time = max(time, t)

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                fresh -= 1
                queue.append((nr, nc, t + 1))

    return time if fresh == 0 else -1

