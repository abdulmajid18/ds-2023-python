def zero_matrix(matrix):
    m, n = len(matrix), len(matrix[0])
    row_set, col_set = set(), set()

    # Identify which rows & columns need to be zeroed
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                row_set.add(i)
                col_set.add(j)

    # Zero out rows
    for i in row_set:
        matrix[i] = [0] * n

    # Zero out columns
    for j in col_set:
        for i in range(m):
            matrix[i][j] = 0
