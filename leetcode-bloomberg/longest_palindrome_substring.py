def longest_palindrome(self, string):
    result_len = 0
    result_str = ""

    max_length = len(string)

    for i in range(max_length):
        l = i
        r = i
        while l >= 0 and r < max_length and string[l] == string[r]:
            if (r - l) + 1 > result_len:
                result_len = (r - l) + 1
                result_str = string[l:r + 1]
            l -= 1
            r += 1

        l = i
        r = i + 1
        while l >= 0 and r < max_length and string[l] == string[r]:
            if (r - l) + 1 > result_len:
                result_len = (r - l) + 1
                result_str = string[l:r + 1]
            l -= 1
            r += 1

    return result_str