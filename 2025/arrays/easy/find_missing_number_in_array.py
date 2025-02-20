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
