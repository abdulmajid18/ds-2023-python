from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def is_valid(board, row, col, num):
            # Check if `num` is not in the current row
            if num in board[row]:
                return False

            # Check if `num` is not in the current column
            for r in range(9):
                if board[r][col] == num:
                    return False

            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(9):
                r = start_row + i // 3
                c = start_col + i % 3
                if board[r][c] == num:
                    return False

            return True

        def dfs(board):
            for row in range(9):
                for col in range(9):
                    if board[row][col] == '.':
                        for num in range(1, 10):
                            num_str = str(num)
                            if is_valid(board, row, col, num_str):
                                board[row][col] = num_str
                                if dfs(board):
                                    return True
                                board[row][col] = '.'  # Reset on backtrack
                        return False  # Trigger backtracking
            return True  # Sudoku solved

        dfs(board)
