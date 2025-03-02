def is_rotation(s1: str, s2: str) -> bool:
    if len(s1) != len(s2) or not s1:
        return False

    return s2 in (s1 + s1)  # Using isSubstring (Python's 'in' operator)


# Example Tests
print(is_rotation("waterbottle", "erbottlewat"))  # True
print(is_rotation("hello", "lohel"))  # True
print(is_rotation("hello", "olelh"))  # False
print(is_rotation("abc", "bca"))  # True
print(is_rotation("abcd", "acbd"))  # False
