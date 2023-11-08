import heapq


def frequencySortOptimized(s):
    char_count = {}  # Dictionary to store character frequencies

    # Count the frequency of each character
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    max_heap = []  # Max heap to store characters based on frequency

    # Push characters into the max heap with frequency as the key
    for char, count in char_count.items():
        heapq.heappush(max_heap, (-count, char))

    sorted_chars = []

    # Pop characters from the max heap and append to the result
    while max_heap:
        count, char = heapq.heappop(max_heap)
        sorted_chars.append(char * (-count))

    sorted_str = ''.join(sorted_chars)

    return sorted_str


def frequencySort2(self, s: str) -> str:
    char_count = {}  # Dictionary to store character frequencies

    # Count the frequency of each character
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Sort the characters based on their frequency in descending order
    sorted_chars = sorted(s, key=lambda x: (-char_count[x], x))

    # Join the sorted characters to form the sorted string
    sorted_str = ''.join(sorted_chars)

    return sorted_str
