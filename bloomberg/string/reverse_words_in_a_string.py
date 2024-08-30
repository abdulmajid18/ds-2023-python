def reverseWords(s: str) -> str:
    # Step 1: Split the string into words by spaces
    words = s.split()

    # Step 2: Reverse the list of words
    reversed_words = words[::-1]

    # Step 3: Join the reversed words with a single space
    result = ' '.join(reversed_words)

    return result


def reverseWordsOptimized(s: str) -> str:
    # Initialize pointers and a list to hold words
    i = len(s) - 1
    result = []
    print(f"Length:  {i}")
    while i >= 0:
        # Skip any trailing spaces
        while i >= 0 and s[i] == ' ':
            i -= 1

        if i < 0:
            break

        # Find the end of the word
        j = i

        # Move i to the beginning of the word
        while i >= 0 and s[i] != ' ':
            i -= 1
        print(f"I:  {i}    J: {j}")
        # Add the word to the result list
        result.append(s[i + 1:j + 1])

    # Join all words with a single space
    return ' '.join(result)


s = "  the sky is  blue  "
# print(reverseWordsOptimized(s))  # Output: "blue is sky the


def reverseWords(s: str) -> str:
    # Step 1: Reverse the entire string
    s = s[::-1]

    # Step 2: Traverse the reversed string and extract words
    n = len(s)
    result = []
    i = 0
    print(s)
    while i < n:
        # Skip spaces
        while i < n and s[i] == ' ':
            i += 1

        if i >= n:
            break

        # Start of the word
        start = i

        # Move i to the end of the word
        while i < n and s[i] != ' ':
            i += 1

        # Extract the word and reverse it
        word = s[start:i][::-1]
        result.append(word)

    # Step 3: Join the words with a single space
    return ' '.join(result)


# Example usage:
s = "  the sky is  blue  "
print(reverseWords(s))  # Output: "blue is sky the"
