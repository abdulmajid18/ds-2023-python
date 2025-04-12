class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        mappings = {'0': '0', '1': '1', '6': '9', '9': '6', '8': '8'}
        left, right = 0, len(num) - 1

        while left <= right:
            if num[left] not in mappings or num[right] not in mappings:
                return False
            if mappings[num[left]] != num[right]:  # Check if flipped matches
                return False
            left += 1
            right -= 1

        return True


class SolutionBruteForce:
    def isStrobogrammatic(self, num: str) -> bool:
        # Mapping of digits when rotated 180 degrees
        rotated_digits = {'0': '0', '1': '1', '6': '9', '9': '6', '8': '8'}

        transformed = ""

        # Traverse the number in reverse order
        for digit in reversed(num):
            if digit not in rotated_digits:
                return False  # Invalid character
            transformed += rotated_digits[digit]  # Build the rotated number

        return transformed == num  # Check if it matches original
