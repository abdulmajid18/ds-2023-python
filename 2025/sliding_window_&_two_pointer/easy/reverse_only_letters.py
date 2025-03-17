def reverseOnlyLetters(s: str) -> str:
    s = list(s)  # Convert string to a list to modify characters

    left, right = 0, len(s) - 1

    while left < right:
        if not s[left].isalpha():
            left += 1
        elif not s[right].isalpha():
            right -= 1
        else:
            # Swap the letters
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    return ''.join(s)  # Convert the list back to a string


# Test cases
print(reverseOnlyLetters("ab-cd"))  # "dc-ba"
print(reverseOnlyLetters("a-bC-dEf-ghIj"))  # "j-Ih-gfE-dCba"
print(reverseOnlyLetters("Test1ng-Leet=code-Q!"))  # "Qedo1ct-eeLg=ntse-T!"

