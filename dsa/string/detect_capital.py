class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # Check if the whole word is uppercase
        if word.isupper():
            return True
        # Check if the whole word is lowercase
        elif word.islower():
            return True
        # Check if only the first letter is uppercase and the rest are lowercase
        elif word[0].isupper() and word[1:].islower():
            return True
        # If none of the above conditions are met
        return False


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n = len(word)

        # If the word length is 1, it's always valid
        if n == 1:
            return True

        # Check the first character
        is_first_upper = 'A' <= word[0] <= 'Z'  # Check if the first character is uppercase

        # Count uppercase letters
        upper_count = 0
        for i in range(n):
            if 'A' <= word[i] <= 'Z':
                upper_count += 1

        # Check conditions based on the number of uppercase letters
        if upper_count == n:  # All uppercase
            return True
        elif upper_count == 0:  # All lowercase
            return True
        elif upper_count == 1 and is_first_upper:  # Only the first is uppercase
            return True

        return False  # All other cases are invalid


# Example usage
solution = Solution()
print(solution.detectCapitalUse("USA"))  # Output: True
print(solution.detectCapitalUse("FlaG"))  # Output: False
print(solution.detectCapitalUse("Google"))  # Output: True
print(solution.detectCapitalUse("leetcode"))  # Output: True

