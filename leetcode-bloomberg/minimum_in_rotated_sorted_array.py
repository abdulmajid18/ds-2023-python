
def minimum_rotated_1(elements):
    l = 0
    r = len(elements)

    while l < r and elements[l] >= elements[r]:
        m = (l + r) / 2
        if elements[r] < elements[m]:
            l = m + 1
        else:
            r = m
    return elements[l]