def are_one_edit_different(s1, s2):
    """Check if a string can converted to another string with a single edit"""
    if len(s1) == len(s2):
        return one_edit_replace(s1, s2)
    if len(s1) + 1 == len(s2):
        return one_edit_insert(s1, s2)
    if len(s1) - 1 == len(s2):
        return one_edit_insert(s2, s1)  # noqa
    return False


def one_edit_replace(s1, s2):
    edit = False
    for i, j in zip(s1, s2):
        if s1[i] != s2[j]:
            if edit:
                return False
            edit = True
    return True

def one_edit_insert(s1, s2):
    edit = False
    i = 0
    j = 0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if edit:
                return False
            edit = True
            j += 1
        else:
            j += 1
            i += 1
    return True

