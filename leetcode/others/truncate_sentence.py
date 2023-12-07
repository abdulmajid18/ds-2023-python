def truncateSentence(s, k):
    # Split the input sentence into words
    words = s.split()

    # Check if the number of words is greater than or equal to k
    if len(words) >= k:
        return " ".join(words[:k])  # Join the first k words and return as a string
    else:
        return s  # Return the original sentence if k is greater than the number of words


# Example usage:
s = "Hello how are you Contestant"
k = 4
truncated = truncateSentence(s, k)
print(truncated)  # Output: "Hello how are you"
