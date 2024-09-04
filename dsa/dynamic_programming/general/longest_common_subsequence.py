a = "ab"
c = "abs"

n = [[0 for j in range(len(c) + 1)] for i in range(len(a) + 1)]

print(n)


def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)
    dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
    print(dp)
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
    return dp[0][0]


def longestCommonSubsequence2(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


"""To solve the Longest Common Subsequence (LCS) problem, we can use dynamic programming. The idea is to build a 2D 
table dp where dp[i][j] will store the length of the LCS of the sequences a[0...i-1] and b[0...j-1].

Here's how we can approach this problem:

Steps:
Initialize a 2D DP array:

Create a 2D array dp of size (n+1) x (m+1) where n and m are the lengths of sequences a and b, respectively. 
Initialize all values to 0. Fill the DP table:

Iterate over the sequences. If a[i-1] == b[j-1], then dp[i][j] = dp[i-1][j-1] + 1 (this means the current element in 
both sequences is part of the LCS). Otherwise, take the maximum value from the previous computations, i.e., 
dp[i][j] = max(dp[i-1][j], dp[i][j-1]). Reconstruct the LCS:

Start from dp[n][m] and trace back the sequence. If a[i-1] == b[j-1], then that element is part of the LCS. Continue 
tracing until you reach the beginning of the sequences. Return the LCS:

Print the LCS.
"""


def longestCommonSubsequenceArray(a, b):
    n, m = len(a), len(b)
    # Create a dp table initialized with 0s
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Fill the dp table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruct the LCS
    i, j = n, m
    lcs = []

    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            lcs.append(a[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    # The lcs list will be in reverse order
    lcs.reverse()

    return lcs


# Input processing
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Get the longest common subsequence
result = longestCommonSubsequence(a, b)

# Print the result
print(' '.join(map(str, result)))
