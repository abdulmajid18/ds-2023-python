from typing import List


def remove_1(elements: List):
    result = set()
    for i in elements:
        result.add(i)
    print(result)
    return len(result)


def remove_2(elements: List):
    l = 1
    for i in range(1, len(elements)):
        if elements[i] != elements[i - 1]:
            elements[l] = elements[i]
            l += 1
    return l


def remove_3(elements: List):
    if len(elements) < 2:
        return len(elements)

    i = 0
    j = 1

    while j < len(elements):
        if elements[i] != elements[j]:
            i += 1
            elements[i] = elements[j]
        j += 1
    return j + 1






if __name__ == '__main__':
    x = [1, 1, 2]
    ans = remove_1(x)
    print(ans)
    ans_2 = remove_2(x)
    print(ans_2)
