from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascal = [[1]]  # Start with the first row

        for i in range(1, rowIndex + 1):
            row = [1]  # First element is always 1
            for j in range(1, i):  # Compute the middle elements
                row.append(pascal[i - 1][j - 1] + pascal[i - 1][j])
            row.append(1)  # Last element is always 1
            pascal.append(row)  # Add new row to Pascal's Triangle

        return pascal[rowIndex]  # Return the desired row


# Example usage
sol = Solution()
print(sol.getRow(3))  # Output: [1, 3, 3, 1]
print(sol.getRow(4))  # Output: [1, 4, 6, 4, 1]


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]

        for i in range(rowIndex):
            next_row = [0] * (len(res) + 1)
            for j in range(len(res)):
                next_row[j] += res[j]
                next_row[j+1] += res[j]
            res = next_row
        return res


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1] * (rowIndex + 1)  # Initialize row with 1s

        for i in range(1, rowIndex):
            for j in range(i, 0, -1):  # Update row from right to left
                row[j] += row[j - 1]

        return row


# Example usage
sol = Solution()
print(sol.getRow(3))  # Output: [1, 3, 3, 1]
print(sol.getRow(4))  # Output: [1, 4, 6, 4, 1]
