def frequencySort(s):
    # Create a dictionary to store character frequencies
    char_freq = {}

    # Count character frequencies
    for char in s:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1

    # Sort characters by their frequency (descending order)
    sorted_chars = sorted(char_freq.keys(), key=lambda x: char_freq[x], reverse=True)

    # Build the sorted string
    result = []
    for char in sorted_chars:
        result.append(char * char_freq[char])

    # Join the characters to form the final sorted string
    return "".join(result)


# Example usage:
s = "tree"
sorted_s = frequencySort(s)
print(sorted_s)  # Output: "eert" or "eetr" (both are correct)
