def one_away(s1: str, s2: str) -> bool:
    # Length difference check
    if abs(len(s1) - len(s2)) > 1:
        return False

    # Identify shorter and longer string
    if len(s1) > len(s2):
        longer, shorter = s1, s2
    else:
        longer, shorter = s2, s1

    i, j = 0, 0  # Pointers for both strings
    found_difference = False

    while i < len(shorter) and j < len(longer):
        if shorter[i] != longer[j]:
            if found_difference:  # More than one edit found
                return False
            found_difference = True

            if len(shorter) == len(longer):  # Replacement case
                i += 1
        else:
            i += 1  # Move pointer for shorter string

        j += 1  # Always move pointer for longer string

    return True


# Example Test Cases
print(one_away("pale", "ple"))  # True (Remove 'a')
print(one_away("pales", "pale"))  # True (Insert 's')
print(one_away("pale", "bale"))  # True (Replace 'p' with 'b')
print(one_away("pale", "bake"))  # False (Needs 2 edits: 'p'->'b', 'l'->'k')
