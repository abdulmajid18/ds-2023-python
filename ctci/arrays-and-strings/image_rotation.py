from typing import List


def rotate_image(matrix: List[List]):
    matrix.reverse()
    N = len(matrix)
    for r in range(N):
        for c in range(r):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
 