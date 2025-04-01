from typing import List

class Solution:
    def rotateBruteForce(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        Brute force approach: Create a new matrix and copy elements.
        """
        n = len(matrix)
        rotated = [[0] * n for _ in range(n)]  # Create a new matrix

        for r in range(n):
            for c in range(n):
                rotated[c][n - 1 - r] = matrix[r][c]  # Place element in new position

        # Copy the rotated matrix back to the original matrix
        for r in range(n):
            for c in range(n):
                matrix[r][c] = rotated[r][c]


from typing import List


class SolutionOptimal:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # Step 1: Transpose the matrix (swap matrix[i][j] with matrix[j][i])
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for row in matrix:
            row.reverse()

