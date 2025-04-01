from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        res = [[matrix[r][c] for c in range(len(matrix[0]))] for r in range(len(matrix))]

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    for i in range(len(matrix[0])):
                        res[r][i] = 0
                    for j in range(len(matrix)):
                        res[j][c] = 0

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                matrix[r][c] = res[r][c]


class SolutionBruteForce:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Step 1: Create a copy of the original matrix
        copy_matrix = [row[:] for row in matrix]  # Deep copy

        rows, cols = len(matrix), len(matrix[0])

        # Step 2: Identify rows and columns to be zeroed
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    # Set entire row to zero in copy
                    for i in range(cols):
                        copy_matrix[r][i] = 0
                    # Set entire column to zero in copy
                    for j in range(rows):
                        copy_matrix[j][c] = 0

        # Step 3: Copy the modified copy_matrix back to matrix
        for r in range(rows):
            for c in range(cols):
                matrix[r][c] = copy_matrix[r][c]  # Update original matrix


from typing import List

class SolutionOptimized:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, col = len(matrix), len(matrix[0])
        rowZero = False

        # Step 1: Mark zeroes in the first row & first column
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0  # Mark column

                    if r > 0:
                        matrix[r][0] = 0  # Mark row
                    else:
                        rowZero = True  # Track if first row itself should be zeroed

        # Step 2: Set cells to zero based on markers
        for r in range(1, row):  # Start from 1 to avoid overwriting markers
            for c in range(1, col):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # Step 3: Handle first column separately
        if matrix[0][0] == 0:
            for r in range(row):
                matrix[r][0] = 0

        # Step 4: Handle first row separately
        if rowZero:
            for c in range(col):
                matrix[0][c] = 0

