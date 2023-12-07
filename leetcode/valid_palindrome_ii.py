def isPalindrome(string: str, low: int, high: int) -> bool:
    while low < high:
        if string[low] != string[high]:
            return False
        low += 1
        high -= 1
    return True


def valid_palindrome(s):
    start = 0
    end = len(s) - 1

    while start < end:
        if s[start] == s[end]:
            start += 1
            end -= 1
        else:
            return (isPalindrome(s, start + 1, end) or
                    isPalindrome(s, start, end - 1))

    return True

def valid_palindrome_2(s):
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            skipL = s[l+1: r+1]
            skipR = s[l:r]
            return skipL == skipL[::-1] or skipR == skipR[::-1]
        l += 1
        r -= 1
    return True

if __name__ == '__main__':
    ans = valid_palindrome('aba')
    print(ans)
