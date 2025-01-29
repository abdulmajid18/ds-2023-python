
from collections import defaultdict

def group_anagrams(strs):
    anagrams = defaultdict(list)
    for word in strs:
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)
    return list(anagrams.values())


from collections import defaultdict

def group_anagrams(strs):
    anagrams = defaultdict(list)
    for word in strs:
        # Create a count of each character (assuming only lowercase English letters)
        count = [0] * 26
        for char in word:
            count[ord(char) - ord('a')] += 1
        # Use the tuple of counts as the key
        anagrams[tuple(count)].append(word)
    return list(anagrams.values())
