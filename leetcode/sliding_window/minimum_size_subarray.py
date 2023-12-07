def minimumSizeBrute(nums, target):
    minLength = float("inf")
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            summ = sum(nums[i:j + 1])
            if summ == target:
                length = (j + 1) - i
                minLength = min(length, minLength)
    return minLength


def minimumSizeBrute2(nums, target):
    minLength = float("inf")
    for i in range(len(nums)):
        currentSum = 0
        for j in range(i, len(nums)):
            currentSum += nums[j]
            if currentSum >= target:
                length = (j + 1) - i
                minLength = min(length, minLength)
    return minLength


def min_subarray_len2(target, nums):
    n = len(nums)
    minLength = float("inf")

    # Calculate cumulative sums
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]

    for i in range(n):
        for j in range(i + 1, n + 1):
            subarray_sum = prefix_sum[j] - prefix_sum[i]
            if subarray_sum >= target:
                minLength = min(minLength, j - i)

    return minLength if minLength != float("inf") else 0


def min_subarray_len_optimized1(target, nums):
    l, total = 0, 0
    res = float("inf")

    for r in range(len(nums)):
        total += nums[r]

        while total >= target:
            res = min(r - l + 1, res)
            total -= nums[l]
            l += 1
    return 0 if res == float("inf") else res


def min_subarray_len_optimized(target, nums):
    # Initialize variables
    min_len = float('inf')  # Initialize to positive infinity
    left = 0  # Left pointer
    current_sum = 0

    for right in range(len(nums)):
        current_sum += nums[right]

        # Check if the current subarray sum is greater than or equal to the target
        while current_sum >= target:
            min_len = min(min_len, right - left + 1)  # Update the minimum length
            current_sum -= nums[left]  # Remove the leftmost element from the subarray
            left += 1  # Move the left pointer to the right

    # If min_len is still positive infinity, there is no valid subarray
    return min_len if min_len != float('inf') else 0


if __name__ == "__main__":
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    result = minimumSizeBrute2(nums, target)
    print("Minimum size subarray sum:", result)
