def longest_1(string):
    char_set = set()
    l = 0
    res = 0

    for r in range(len(string)):
        while string[r] in char_set:
            char_set.remove(string[l])
            l += 1
        char_set.add(string[r])
        res = max(res, r - l + 1)
    return res;


def longest_2(string):
    exists = [False] * 256
    i = 0
    max_len = 0
    for j in range(len(string)):
        while exists[ord(string[j])]:
            exists[ord(string[j])] = False
            i += 1
        exists[ord(string[j])] = True
        max_len = max(max_len, j - i + 1)
    return max_len


def length_of_longest_substring(s):
    char_index_map = {}  # Dictionary to store the index of each character in the current substring
    max_length = 0
    start_index = 0  # Start index of the current substring

    for end_index, char in enumerate(s):
        # If the character is already in the current substring, update the start index
        if char in char_index_map and char_index_map[char] >= start_index:
            start_index = char_index_map[char] + 1

        # Update the index of the current character
        char_index_map[char] = end_index

        # Update the maximum length if needed
        max_length = max(max_length, end_index - start_index + 1)

    return max_length


if __name__ == '__main__':
    ans = longest_2('bbbb')
    print(ans)
