from typing import List


def sortArray(nums: List[int]) -> List[int]:
    def merge_sort(arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)

    def merge(left: List[int], right: List[int]) -> List[int]:
        merged = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        while i < len(left):
            merged.append(left[i])
            i += 1

        while j < len(right):
            merged.append(right[j])
            j += 1

        return merged

    return merge_sort(nums)


from typing import List


def sortArrayInplace(nums: List[int]) -> List[int]:

    def merge(arr: List[int], L: int, M: int, R: int) -> None:
        left = arr[L:M+1]
        right = arr[M+1:R+1]

        i = j = 0
        k = L

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    def mergeSort(arr: List[int], l: int, r: int) -> None:
        if l >= r:
            return

        m = (l + r) // 2
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)

    mergeSort(nums, 0, len(nums) - 1)
    return nums
