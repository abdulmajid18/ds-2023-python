from typing import List
import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize hash sets for rows, columns, and 3x3 subgrids
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # key = (r // 3, c // 3)

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == ".":
                    continue
                if (num in rows[r] or num in cols[c] or num in squares[(r // 3, c // 3)]):
                    return False
                rows[r].add(num)
                cols[c].add(num)
                squares[(r // 3, c // 3)].add(num)

        return True
