from typing import List


class Solution:
    def searchMatrixBruteForce(self, matrix: List[List[int]], target: int) -> bool:
        # Check for empty matrix
        if not matrix or not matrix[0]:
            return False

        # Iterate through each element in the matrix
        for row in matrix:
            for element in row:
                if element == target:
                    return True

        # If the target is not found
        return False


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        rows, cols = len(matrix), len(matrix[0])
        row, col = 0, cols - 1  # Start from top-right corner

        while row < rows and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1  # Move left
            else:
                row += 1  # Move down

        return False
