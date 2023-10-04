def fist_unique(s):
    import collections

    counter = collections.Counter(list(s))

    for i in range(len(s)):
        if counter.get(s[i]) == 1:
            return i
    return -1


def first_unique_char_optimized(s):
    map = [0] * 128

    for i in s:
        map[ord(i)] += 1

    for j in s:
        if map[ord(j)] == 1:
            print(j)





if __name__ == '__main__':
    first_unique_char_optimized("abcba")