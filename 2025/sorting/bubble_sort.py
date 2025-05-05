def bubble_sort(nums):
    """
    In-place, stable Bubble Sort.
    Worst-time  : O(n^2)
    Best-time   : O(n)      (already sorted, thanks to 'swapped' flag)
    Space       : O(1)
    """
    n = len(nums)

    for p in range(n - 1):
        swapped = False

        for i in range(n - 1 - p):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True

        if not swapped:  # no swap ⇒ sorted
            break
