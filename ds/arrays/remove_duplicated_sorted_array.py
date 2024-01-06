from typing import List


def remove_1(elements: List):
    result = set()
    for i in elements:
        result.add(i)
    print(result)
    return len(result)

def remove_4(elements):
    l = 1

    for r in range(1, len(elements)):
        if elements[r] != elements[r-1]:
            elements[l] = elements[r]
            l += 1

    return l + 1

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


from typing import List

def remove_duplicates(nums: List[int]) -> int:
    if not nums:
        return 0  # Empty array

    # Initialize two pointers
    i, j = 0, 1

    # Iterate through the array
    while j < len(nums):
        # If the current element is different from the previous one
        if nums[j] != nums[i]:
            # Move the i pointer forward
            i += 1
            # Update the i-th element with the j-th element
            nums[i] = nums[j]
        # Move the j pointer forward
        j += 1

    # The length of the modified array is (i + 1)
    return i + 1

# Example usage:
nums = [1, 1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 5]
result_length = remove_duplicates(nums)
print("Modified Array:", nums[:result_length])





if __name__ == '__main__':
    x = [1, 1, 2]
    ans = remove_1(x)
    print(ans)
    ans_2 = remove_2(x)
    print(ans_2)
