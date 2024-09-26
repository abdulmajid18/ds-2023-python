from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        current = 1

        for _ in range(n):
            result.append(current)

            if current * 10 <= n:
                current *= 10  # Try to go deeper by appending a '0'
            else:
                # Find the next lexicographical number by adding 1
                while current % 10 == 9 or current + 1 > n:
                    current //= 10  # Move back up in the tree
                current += 1  # Increment the current number

        return result
