from typing import List

def set_zerosA(matrix:List[List[int]]):
    ROWS, COLS = len(matrix), len(matrix[0])
    rowZero = False

    for r in range(ROWS):
        for c in range(COLS):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                if r > 0:
                    matrix[r][0] = 0
                else:
                    rowZero = True
    for r in range(1,ROWS):
        for c in range(1,COLS):
            if matrix[0][r] == 0 or matrix[r][0]:
                matrix[r][c] = 0

    if matrix[0][0] == 0:
        for r in range(ROWS):
            matrix[r][0] = 0

    if rowZero:
        for c in range(COLS):
            matrix[0][c] = 0


def set_zeros(matrix:List[List[int]]):
    M, N = len(matrix), len(matrix[0])
    row, col = [1]*M, [1]*N

    for r in range(M):
        for c in range(N):
            if matrix[r][c] == 0:
                row[r] = 0
                col[c] = 0

    # update
    for r in range(M):
        if row[r] == 0:
            matrix[r] = [0]*N

    for c in range(N):
        if col[c] == 0:
            for i in range(M):
                matrix[i][c] = 0

    return matrix


def zero_matrix(matrix):
    m = len(matrix)
    n = len(matrix[0])

    rows = set()
    cols = set()

    for x in range(m):
        for y in range(n):
            if matrix[x][y] == 0:
                rows.add(x)
                cols.add(y)

    for x in range(m):
        for y in range(n):
            if (x in rows) or (y in cols):
                matrix[x][y] = 0

    return  matrix

if __name__ == '__main__':
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    ans = set_zeros(matrix)
    print(ans)
    matrix_2 = [[1,1,1],[1,0,1],[1,1,1]]
    ans_2 = zero_matrix(matrix_2)
    print(ans)