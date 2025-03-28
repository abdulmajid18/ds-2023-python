class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0  # i for word, j for abbr
        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():  # If it's a number
                if abbr[j] == '0':  # Leading zero is not allowed
                    return False
                steps = 0
                while j < len(abbr) and abbr[j].isdigit():  # Convert number
                    steps = steps * 10 + int(abbr[j])
                    j += 1
                i += steps  # Move `i` forward by `num`
            else:  # If it's a character
                if word[i] != abbr[j]:  # Mismatch
                    return False
                i += 1
                j += 1

        return i == len(word) and j == len(abbr)


sol = Solution()

# Standard cases with correct abbreviations
print(sol.validWordAbbreviation("internationalization", "i12iz4n"))  # True
print(sol.validWordAbbreviation("substitution", "s10n"))  # True
print(sol.validWordAbbreviation("apple", "a4"))  # True
print(sol.validWordAbbreviation("banana", "b4a"))  # True
print(sol.validWordAbbreviation("character", "c7r"))  # True
