class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i == m - 1 and j == n - 1:
                return 1

            if i >= m or j >= n:
                return 0

            memo[(i, j)] = dfs(i + 1, j) + dfs(i, j + 1)
            return memo[(i, j)]

        return dfs(0, 0)


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]
