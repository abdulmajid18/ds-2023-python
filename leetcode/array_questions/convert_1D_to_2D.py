def construct2DArray(original, m, n):
    # Check if the size of original is equal to m * n
    if len(original) != m * n:
        return []

    # Initialize the 2D array with zeros
    result = [[0] * n for _ in range(m)]

    # Fill the 2D array row by row
    for i in range(m):
        for j in range(n):
            result[i][j] = original[i * n + j]

    return result
