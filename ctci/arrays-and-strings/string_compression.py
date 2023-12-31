 # aabcccccaaa would become a2blc5a3.

def compress_string(string):
    compressed = []
    counter = 0

    for i in range(len(string)):  # noqa
        if i != 0 and string[i] != string[i - 1]:
            compressed.append(string[i - 1] + str(counter))
            counter = 0
        counter += 1

    # add last repeated character
    if counter:
        compressed.append(string[-1] + str(counter))

    # returns original string if compressed string isn't smaller
    return min(string, "".join(compressed), key=len)




if __name__ == '__main__':
    ans = compress_string("aabcccccaaa")
    print(ans)


