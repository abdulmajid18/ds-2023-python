
def minimum_rotated_1(elements):
    l = 0
    r = len(elements)

    while l < r and elements[l] >= elements[r]:
        m = (l + r) / 2
        if elements[m] > elements[r]:
            l = m + 1
        elif elements[m] < elements[l]:
            r = m
        else:
            l = l + 1
    return elements[l]