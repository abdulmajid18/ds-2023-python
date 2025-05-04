from typing import List


def maxScoreBruteForce(cardPoints: List[int], k: int) -> int:
    n = len(cardPoints)
    max_score = 0

    for i in range(k + 1):  # take i from the front, k-i from the back
        front = sum(cardPoints[:i])
        back = sum(cardPoints[n - (k - i):])
        max_score = max(max_score, front + back)

    return max_score

