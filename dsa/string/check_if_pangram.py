class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        table = [False] * 26  # Initialize a list of 26 False values, one for each letter of the alphabet

        for char in sentence:
            if 'a' <= char <= 'z':  # Ensure only lowercase letters are processed
                ascii_val = ord(char) - ord("a")  # Calculate the index for the letter
                table[ascii_val] = True  # Mark the letter as seen

        return all(table)  # If all letters are seen, return True
