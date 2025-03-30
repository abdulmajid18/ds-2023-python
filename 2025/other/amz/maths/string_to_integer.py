class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        sign = 1
        i = 0
        if s[0] == "-" or s[0] == '+':
            if s[0] == '-':
                sign = -1
            i += 1

        res = 0
        while i < len(s) and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1

        res *= sign

        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1

        if res < INT_MIN:
            return INT_MIN
        if res > INT_MAX:
            return INT_MAX

        return res

    
sol = Solution()

print(sol.myAtoi("42"))  # Output: 42
print(sol.myAtoi("   -42"))  # Output: -42
print(sol.myAtoi("4193 with words"))  # Output: 4193
print(sol.myAtoi("words and 987"))  # Output: 0
print(sol.myAtoi("+1"))  # Output: 1

print(sol.myAtoi(""))  # Output: 0 (Empty input)
print(sol.myAtoi("+-12"))  # Output: 0 (Invalid format)
print(sol.myAtoi("00000-42a1234"))  # Output: 0
print(sol.myAtoi("21474836460"))  # Output: 2147483647 (Clamped to max)
print(sol.myAtoi("-91283472332"))  # Output: -2147483648 (Clamped to min)
