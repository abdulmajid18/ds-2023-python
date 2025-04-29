from typing import List


def totalFruitBruteForce(fruits):
    n = len(fruits)
    max_len = 0

    for i in range(n):
        types = set()
        for j in range(i, n):
            types.add(fruits[j])
            if len(types) > 2:
                break
            max_len = max(max_len, j - i + 1)

    return max_len


# Test the function
fruits = [1, 2, 1]
print(totalFruitBruteForce(fruits))  # Output: 3

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        from collections import defaultdict
        count = defaultdict(int)
        l, total = 0, 0
        res = 0

        for r, v in enumerate(fruits):
            count[v] += 1
            total += 1

            while len(count) > 2:
                f = fruits[l]
                count[f] -= 1
                total -= 1

                if not count[f]:
                    count.pop(f)

                l += 1

            res = max(res, total)
        return res

