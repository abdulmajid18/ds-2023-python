from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        #  transpose the matrix
        for i in range(n): # n = 3 (0, 1, 2)
            for j in range(i, n):  # (0, 1, 2), (1,2), (2)
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        #  reverse
        for e in matrix:
            e.reverse()