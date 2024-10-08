class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        table = [False] * 26  # Initialize a list of 26 False values, one for each letter of the alphabet

        for char in sentence:
            if 'a' <= char <= 'z':  # Ensure only lowercase letters are processed
                ascii_val = ord(char) - ord("a")  # Calculate the index for the letter
                table[ascii_val] = True  # Mark the letter as seen

        return all(table)  # If all letters are seen, return True


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        seen_chars = set()

        for char in sentence:
            if 'a' <= char <= 'z':  # Check if the character is a lowercase letter
                seen_chars.add(char)

            # Early exit if all letters are found
            if len(seen_chars) == 26:
                return True

        return len(seen_chars) == 26  # Check if all 26 letters are present


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # List of all letters in the English alphabet
        alphabet = 'abcdefghijklmnopqrstuvwxyz'

        # Check each letter in the alphabet
        for letter in alphabet:
            if letter not in sentence:
                return False  # Return False if any letter is missing

        return True  # Return True if all letters are found
