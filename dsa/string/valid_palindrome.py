class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Normalize the string by filtering out non-alphanumeric characters and converting to lowercase
        filtered_chars = [char.lower() for char in s if char.isalnum()]

        # Check if the filtered string is equal to its reverse
        return filtered_chars == filtered_chars[::-1]


# Example Usage
solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))  # Output: True
print(solution.isPalindrome("race a car"))  # Output: False


def isPalindrome2(s):
    new_str = ""

    for c in s:
        if c.isalnum():
            new_str += c.lower()

    return new_str == new_str[::-1]


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            # Move left pointer to the right if not alphanumeric
            while left < right and not s[left].isalnum():
                left += 1
            # Move right pointer to the left if not alphanumeric
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare the characters at left and right pointers
            if s[left].lower() != s[right].lower():
                return False

            # Move both pointers inward
            left += 1
            right -= 1

        return True


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            # Move left pointer to the right if not alphanumeric
            while left < right and not self.is_alphanumeric(s[left]):
                left += 1
            # Move right pointer to the left if not alphanumeric
            while left < right and not self.is_alphanumeric(s[right]):
                right -= 1

            # Compare the characters at left and right pointers
            if s[left].lower() != s[right].lower():
                return False

            # Move both pointers inward
            left += 1
            right -= 1

        return True

    def is_alphanumeric(self, c: str) -> bool:
        return ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9')


