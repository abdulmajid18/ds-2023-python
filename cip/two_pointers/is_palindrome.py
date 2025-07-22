def is_palindrome_valid(s: str) -> bool:
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True

def is_palindrome_valid_brute_force(s: str) -> bool:
    cleaned = []
    stack = []

    for char in s:
        if char.isalnum():
            lower_char = char.lower()
            cleaned.append(lower_char)
            stack.append(lower_char)

    for char in cleaned:
        if char != stack.pop():
            return False

    return True
