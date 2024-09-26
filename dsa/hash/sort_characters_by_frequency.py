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


def frequencySort(s: str) -> str:
    # Step 1: Count the frequency of each character using a hashmap (dictionary)
    frequency = {}
    for char in s:
        frequency[char] = frequency.get(char, 0) + 1

    # Step 2: Create buckets for each frequency
    # The maximum frequency can be at most the length of the string
    max_freq = len(s)
    buckets = [[] for _ in range(max_freq + 1)]

    # Step 3: Fill the buckets
    for char, freq in frequency.items():
        buckets[freq].append(char)

    # Step 4: Build the result string
    result = []
    # Iterate over the buckets from the highest frequency to the lowest
    for freq in range(max_freq, 0, -1):
        if buckets[freq]:  # Check if there are characters with this frequency
            for char in buckets[freq]:
                result.append(char * freq)  # Append the character freq times

    return ''.join(result)

# Example usage
s = "tree"
result = frequencySort(s)
print(result)  # Output: "eetr" or "eert", depending on the order of characters
