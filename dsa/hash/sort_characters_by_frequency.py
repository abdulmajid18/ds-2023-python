import heapq


def frequencySort(s: str) -> str:
    # Step 1: Count the frequency of each character using a hashmap (dictionary)
    frequency = {}
    for char in s:
        frequency[char] = frequency.get(char, 0) + 1

    # Step 2: Build a max-heap based on character frequencies
    max_heap = []
    for char, freq in frequency.items():
        # Push negative frequency to simulate max-heap
        heapq.heappush(max_heap, (-freq, char))

    # Step 3: Build the result string based on the frequencies
    result = []
    while max_heap:
        freq, char = heapq.heappop(max_heap)
        result.append(char * -freq)  # Append the character frequency times

    return ''.join(result)


# Example usage
s = "tree"
result = frequencySort(s)
print(result)  # Output: "eetr" or "eert", depending on the order of characters
