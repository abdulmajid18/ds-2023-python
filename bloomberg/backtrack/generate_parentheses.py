"""

The "Generate Parentheses" problem on LeetCode (Problem 22) requires generating all combinations of well-formed parentheses for a given number n pairs of parentheses.

Problem Statement:
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example:
plaintext
Copy code
Input: n = 3
Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]
Approach:
The problem can be solved using backtracking. The idea is to build the string of parentheses one character at a time, ensuring that at any point:

We do not add more closing parentheses ) than opening parentheses (.
We only add a closing parenthesis ) if there is an unmatched opening parenthesis.
Backtracking Algorithm:
Start with an empty string and two counters: open for the number of ( used and close for the number of ) used.
If open is less than n, you can add an opening parenthesis (.
If close is less than open, you can add a closing parenthesis ).
Recursively build the string until both open and close equal n.
Add the valid string to the result list.
Python Implementation:
python
Copy code
from typing import List

class Solution:
    def generateParentheses(self, n: int) -> List[str]:
        def backtrack(s='', open=0, close=0):
            # If the string s is a valid combination, add to the result
            if len(s) == 2 * n:
                result.append(s)
                return

            # If we can add an opening parenthesis, add it and backtrack
            if open < n:
                backtrack(s + '(', open + 1, close)

            # If we can add a closing parenthesis, add it and backtrack
            if close < open:
                backtrack(s + ')', open, close + 1)

        result = []
        backtrack()  # Start the backtracking with an empty string
        return result
Explanation:
backtrack Function: The function takes three arguments:

s: the current string being built.
open: the number of opening parentheses used.
close: the number of closing parentheses used.
It generates the combinations by recursively trying to add either an opening or closing parenthesis while ensuring the combination remains valid.

Base Case: When the length of s reaches 2 * n, it means a valid combination is formed, so it is added to the result list.

Recursion: The function tries to add ( if open < n and ) if close < open, ensuring that the parentheses are balanced.
"""
from typing import List


def generateParenthesis(self, n: int) -> List[str]:
    result = []

    def backtrack(s='', open=0, close=0):
        # If the string s is a valid combination, add to the result
        if len(s) == 2 * n:
            result.append(s)
            return

        # If we can add an opening parenthesis, add it and backtrack
        if open < n:
            backtrack(s + '(', open + 1, close)

        # If we can add a closing parenthesis, add it and backtrack
        if close < open:
            backtrack(s + ')', open, close + 1)

    backtrack()
    return result