def rotateInplace(nums, k):
    n = len(nums)
    k = k % n

    l, r = 0, n-1

    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, l + r

    l, r = 0, k-1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, l + r

    l, r = k, n-1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, l + r


def rotateBrute1(nums, k):
    n = len(nums)
    k = k % n  # Handle cases where k >= n

    # Create a new array to store the rotated elements
    rotated = [0] * n
    for i in range(n):
        rotated[(i + k) % n] = nums[i]

    # Copy the elements back to the original array
    for i in range(n):
        nums[i] = rotated[i]
