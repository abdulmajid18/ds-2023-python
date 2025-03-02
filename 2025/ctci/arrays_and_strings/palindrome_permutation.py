from collections import Counter


def is_palindrome_permutation(s):
    s = s.lower().replace(" ", "")  # Normalize: Ignore spaces and case
    bit_vector = 0  # This will store character parity (odd/even count)

    for char in s:
        bit_index = ord(char) - ord('a')  # Get index (a=0, b=1, ..., z=25)
        bit_vector ^= (1 << bit_index)  # Toggle the bit

    return bit_vector == 0 or (bit_vector & (bit_vector - 1)) == 0  # At most 1 bit set


# Example Runs
print(is_palindrome_permutation("Tact Coa"))  # True (e.g., "taco cat")
print(is_palindrome_permutation("civic"))  # True
print(is_palindrome_permutation("hello"))  # False
print(is_palindrome_permutation("A Santa at NASA"))  # True


def is_palindrome_permutation_map(s):
    s = s.lower().replace(" ", "")  # Normalize: Ignore spaces and case
    char_counts = Counter(s)  # Count occurrences of each character

    odd_count = sum(1 for count in char_counts.values() if count % 2 == 1)

    return odd_count <= 1  # At most one character should have an odd count


def is_palindrome_permutation_array(s):
    s = s.lower().replace(" ", "")  # Normalize input
    char_counts = [0] * 26  # Array for a-z

    for char in s:
        char_counts[ord(char) - ord('a')] += 1  # Increment count

    odd_count = sum(1 for count in char_counts if count % 2 == 1)

    return odd_count <= 1  # At most one character should have an odd count


