def find_missing_number_bruteforce(arr, N):
    for i in range(1, N + 1):  # Loop from 1 to N
        found = False
        for num in arr:  # Check if i exists in the array
            if num == i:
                found = True
                break
        if not found:  # If i is not found in the array, return it
            return i


# Example usage:
arr = [1, 3]  # N = 3, missing number is 2
N = 3
print(find_missing_number_bruteforce(arr, N))  # Output: 2


def find_missing_number_hashing(arr, N):
    hash_arr = [0] * (N + 1)  # Create a hash array of size N+1 initialized with 0

    # Mark the numbers present in the array
    for num in arr:
        hash_arr[num] = 1

    # Find the missing number
    for i in range(1, N + 1):
        if hash_arr[i] == 0:
            return i  # The missing number


# Example usage:
arr = [1, 3]  # N = 3, missing number is 2
N = 3
print(find_missing_number_hashing(arr, N))  # Output: 2


def find_missing_number_sum(arr, N):
    total_sum = (N * (N + 1)) // 2  # Sum of first N natural numbers
    actual_sum = sum(arr)  # Sum of array elements
    return total_sum - actual_sum  # The missing number

# Example usage:
arr = [1, 2, 4, 5]  # N = 5, missing number is 3
N = 5
print(find_missing_number_sum(arr, N))  # Output: 3
