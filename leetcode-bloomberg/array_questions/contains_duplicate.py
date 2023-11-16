def containsDuplicate(nums):
    # Create an empty set to store unique elements
    unique_set = set()

    # Iterate through the array
    for num in nums:
        # If the element is already in the set, it's a duplicate
        if num in unique_set:
            return True
        # Otherwise, add it to the set
        else:
            unique_set.add(num)

    # If no duplicates are found, return false
    return False

def containsDuplicateB(nums):
    # Sort the array in ascending order
    nums.sort()

    # Check for duplicates by comparing adjacent elements
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True

    # If no duplicates are found, return false
    return False
