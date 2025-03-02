def rotate_matrix(matrix):
    # Step 1: Transpose
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()


def rotate_matrix(matrix):
    n = len(matrix)

    for layer in range(n // 2):  # Process layer by layer
        first, last = layer, n - layer - 1

        for i in range(first, last):
            offset = i - first  # Offset within layer

            # Save top
            top = matrix[first][i]

            # Left -> Top
            matrix[first][i] = matrix[last - offset][first]

            # Bottom -> Left
            matrix[last - offset][first] = matrix[last][last - offset]

            # Right -> Bottom
            matrix[last][last - offset] = matrix[i][last]

            # Top -> Right
            matrix[i][last] = top


# Example Usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotate_matrix(matrix)

for row in matrix:
    print(row)

