def isUnique(s):
    char_set = [False] * 128  # Assuming ASCII characters

    for char in s:
        idx = ord(char)  # Convert character to ASCII index
        if char_set[idx]:  # If already found, it's not unique
            return False
        char_set[idx] = True

    return True  # All characters are unique


def isUniqueUnicode(s):
    char_set = set()  # A set to store seen characters

    for char in s:
        if char in char_set:  # If already found, it's not unique
            return False
        char_set.add(char)

    return True  # All characters are unique


def isUniqueUpperCaseBit(s):
    checker = 0

    for char in s:
        idx = ord(char)-ord("A")
        bit = 1 << idx

        if checker & bit:
            return False

        checker |= bit
    return True


def isUniqueUpperCaseArray(s):
    char_set = [False] * 26  # Only for 'A'-'Z'

    for char in s:
        idx = ord(char) - ord('A')  # Convert 'A'-'Z' to index 0-25
        if char_set[idx]:  # If already seen, return False
            return False
        char_set[idx] = True  # Mark character as seen

    return True  # All characters are unique


def isUniqueBothUpperAndLowerBit(s):
    checker = 0  # Bit vector to track seen characters

    for char in s:
        if 'A' <= char <= 'Z':
            idx = ord(char) - ord('A')  # Index for 'A'-'Z' (0-25)
        elif 'a' <= char <= 'z':
            idx = ord(char) - ord('a') + 26  # Index for 'a'-'z' (26-51)
        else:
            continue  # Ignore non-alphabet characters

        bit = 1 << idx  # Create a bitmask for the character

        if checker & bit:  # If bit is already set, it's a duplicate
            return False

        checker |= bit  # Mark character as seen

    return True  # All characters are unique


def isUniqueBothUpperAndLowerArray(s):
    char_set = [False] * 52  # Array for tracking A-Z and a-z

    for char in s:
        if 'A' <= char <= 'Z':
            idx = ord(char) - ord('A')  # Index for 'A'-'Z' (0-25)
        elif 'a' <= char <= 'z':
            idx = ord(char) - ord('a') + 26  # Index for 'a'-'z' (26-51)
        else:
            continue  # Ignore non-alphabet characters

        if char_set[idx]:  # If character was already seen, return False
            return False

        char_set[idx] = True  # Mark character as seen

    return True  # All characters are unique