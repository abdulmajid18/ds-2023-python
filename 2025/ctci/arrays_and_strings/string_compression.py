def compress_string(s: str) -> str:
    if len(s) <= 1:
        return s  # A single-character string cannot be compressed

    compressed = []
    count = 1

    for i in range(1, len(s)):  # Start from the second character
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1] + str(count))  # Append char + count
            count = 1  # Reset count for the next character

    compressed.append(s[-1] + str(count))  # Append last character + count

    compressed_str = "".join(compressed)  # Convert list to string

    return compressed_str if len(compressed_str) < len(s) else s  # Return shorter one


# Example Test Cases
print(compress_string("aabcccccaaa"))  # Output: "a2b1c5a3"
print(compress_string("abcd"))  # Output: "abcd" (since compressed is not shorter)
print(compress_string("aa"))  # Output: "aa" (since compressed is not shorter)
print(compress_string("aabbcc"))  # Output: "aabbcc" (not shorter)
