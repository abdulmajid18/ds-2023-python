from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True

            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or (r, c) in path):
                return False

            path.add((r, c))
            res = (dfs(r+1, c, i + 1) or
                                dfs(r-1, c, i + 1) or dfs(r, c+1, i + 1) or dfs(r, c-1, i + 1))
            path.remove((r, c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0): return True
        return False


def existInplaceSpace(board: List[List[str]], word: str) -> bool:
    if not board:
        return False

    rows, cols = len(board), len(board[0])

    def dfs(r, c, index):
        # If we have checked the last character in the word, return True
        if index == len(word):
            return True

        # Check boundaries and if the current cell matches the word's character at the index
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]:
            return False

        # Temporarily mark the cell as visited
        temp = board[r][c]
        board[r][c] = '#'

        # Explore all four directions (up, down, left, right)
        found = (dfs(r + 1, c, index + 1) or
                 dfs(r - 1, c, index + 1) or
                 dfs(r, c + 1, index + 1) or
                 dfs(r, c - 1, index + 1))

        # Backtrack: unmark the cell as visited
        board[r][c] = temp

        return found

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True

    return False
