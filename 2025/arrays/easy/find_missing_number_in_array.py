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


def find_missing_number_xor(arr, N):
    """
    XOR Approach to Find the Missing Number in an Array

    Intuition:
    The XOR operation has two important properties:
    1. XOR of two same numbers is always 0:      a ^ a = 0
    2. XOR of a number with 0 is the number itself: 0 ^ a = a

    Using these properties:
    - XOR of numbers from 1 to N: xor1 = 1 ^ 2 ^ ... ^ N
    - XOR of all elements in the given array: xor2 = 1 ^ 2 ^ ... (missing number) ^ ... ^ N

    When we XOR xor1 and xor2, all numbers except the missing one cancel out, leaving only:
    missing_number = xor1 ^ xor2

    Approach:
    1. Initialize two variables: xor1 and xor2.
    2. Compute XOR of numbers from 1 to N (xor1).
    3. Compute XOR of all elements in the array (xor2).
    4. XOR both results to find the missing number.

    Dry Run:
    Given array: [1, 2, 4, 5], N = 5

    XOR of 1 to 5 (xor1)  = (1 ^ 2 ^ 3 ^ 4 ^ 5)
    XOR of array elements (xor2) = (1 ^ 2 ^ 4 ^ 5)

    Result:
    (1 ^ 2 ^ 3 ^ 4 ^ 5) ^ (1 ^ 2 ^ 4 ^ 5)
    = (1^1) ^ (2^2) ^ 3 ^ (4^4) ^ (5^5)
    = 0 ^ 0 ^ 3 ^ 0 ^ 0 = 3 (missing number)

    Complexity:
    - Time Complexity: O(N) (Single pass over array)
    - Space Complexity: O(1) (No extra space used)
    """

    xor1 = 0  # XOR of numbers from 1 to N
    xor2 = 0  # XOR of elements in the array

    # Compute XOR for numbers 1 to N
    for i in range(1, N + 1):
        xor1 ^= i

    # Compute XOR for array elements
    for num in arr:
        xor2 ^= num

    # XOR of xor1 and xor2 gives the missing number
    return xor1 ^ xor2


# Example usage:
arr = [1, 2, 4, 5]  # N = 5, missing number is 3
N = 5
print(find_missing_number_xor(arr, N))  # Output: 3
