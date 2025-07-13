from collections import deque, defaultdict
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        L = len(beginWord)
        all_combo_dict = defaultdict(list)

        for word in wordList:
            for i in range(L):
                pattern = word[:i] + '*' + word[i + 1:]
                all_combo_dict[pattern].append(word)

        queue = deque([(beginWord, 1)])
        visited = set([beginWord])

        while queue:
            current_word, level = queue.popleft()
            for i in range(L):
                pattern = current_word[:i] + '*' + current_word[i + 1:]
                for word in all_combo_dict[pattern]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited.add(word)
                        queue.append((word, level + 1))
                all_combo_dict[pattern] = []

        return 0





