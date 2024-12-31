def three_sum_closest(nums, target):
    nums.sort()  # Sort the array to use a two-pointer approach
    closest_sum = float('inf')  # Initialize the closest sum to infinity

    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            # Update the closest sum if the current one is closer
            if abs(target - current_sum) < abs(target - closest_sum):
                closest_sum = current_sum

            if current_sum < target:
                left += 1  # Move the left pointer to increase the sum
            elif current_sum > target:
                right -= 1  # Move the right pointer to decrease the sum
            else:
                # If the exact target is found, return it
                return current_sum

    return closest_sum


# Example usage:
nums = [-1, 2, 1, -4]
target = 1
print(three_sum_closest(nums, target))  # Output: 2
