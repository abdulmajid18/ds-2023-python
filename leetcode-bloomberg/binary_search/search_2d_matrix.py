def searchMatrix(matrix, target):
    ROWS, COLS = len(matrix), len(matrix[0])

    top, bot = 0, ROWS - 1

    while top <= bot:
        rows = (top + bot) // 2
        if target > matrix[rows][-1]:
            top = rows + 1
        elif target < matrix[rows][0]:
            bot = rows - 1
        else:
            break

    if not (top <= bot):
        return False

    row = (top + bot) // 2
    l, r = 0, COLS - 1
    while l <= r:
        m = (l + r) // 2
        if target > matrix[row][m]:
            l = m + 1
        elif target < matrix[row][m]:
            r = m - 1
        else:
            return True
    return False


def searchMatrix2(matrix, target):
    i = 0
    j = len(matrix[0]) - 1  # number of columns

    while i < len(matrix) and j >= 0:
        if target == matrix[i][j]:
            return True
        elif target < matrix[i][j]:
            j -= 1
        else:
            i += 1

    return False


if __name__ == '__main__':
    # Example usage:
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    target = 3
    print(searchMatrix2(matrix, target))  # Output: True