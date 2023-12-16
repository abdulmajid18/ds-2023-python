def search_and_insert(elements, target):
    left = 0
    right = len(elements) - 1

    while left < right:
        mid = (left + right) // 2
        if elements[mid] > target:
            right = mid
        else:
            left = mid + 1
    if elements[left] < target:
        return left + 1
    return left


def search_and_insert_2(elements, target):
    left = 0
    right = len(elements) - 1

    while left <= right:
        mid = (left + right) // 2
        if elements[mid] == target:
            return mid
        if target > elements[mid]:
            left = mid + 1
        else:
            left = mid - 1
    return left
