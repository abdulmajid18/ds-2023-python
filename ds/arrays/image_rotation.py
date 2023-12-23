from typing import List


def rotate(matrix):
    # Step 1: Transpose the matrix
    n = len(matrix)
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse rows
    for i in range(n):
        matrix[i].reverse()

        # Step 1: Swap rows from top to bottom
    # for i in range(n // 2):
    #     matrix[i], matrix[n - i - 1] = matrix[n - i - 1], matrix[i]

# Example usage:
matrix = [
    [1, 2, 3], [1,4,7]
    [4, 5, 6], [2,5,8]
    [7, 8, 9]  [3,6,9]
]

rotate(matrix)
print(matrix)
