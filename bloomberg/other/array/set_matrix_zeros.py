def setZeroes(matrix):
    if not matrix:
        return
    rows, cols = len(matrix), len(matrix[0])

    row_zero = False

    #  determine which rows and cols need to be zero
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                matrix[0][j] = 0

                if i > 0:
                    matrix[i][0] = 0
                else:
                    row_zero = True

    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[0][j] == 0 or matrix[i][0] == 0:
                matrix[i][j] = 0

    if matrix[0][0] == 0:
        for i in range(rows):
            matrix[i][0] = 0

    if row_zero:
        for j in range(cols):
            matrix[j][0] = 0



