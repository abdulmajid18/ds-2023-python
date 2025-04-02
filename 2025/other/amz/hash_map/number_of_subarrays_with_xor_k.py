class SolutionBruteForce:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        total = 0

        for i in range(len(A)):
            xor_result = 0
            for j in range(i, len(A)):
                xor_result ^= A[j]
                if xor_result == B:
                    total += 1
        return total


from collections import defaultdict


def count_subarrays_with_xor(A, B):
    prefix_xor_count = defaultdict(int)
    prefix_xor = 0
    total = 0

    # Initializing the hashmap with {0:1} for subarrays starting from index 0
    prefix_xor_count[0] = 1

    for num in A:
        prefix_xor ^= num  # Update running prefix XOR

        # If (prefix_xor ⊕ B) is found in hashmap, increment count
        if (prefix_xor ^ B) in prefix_xor_count:
            total += prefix_xor_count[prefix_xor ^ B]

        # Update the hashmap with the current prefix XOR
        prefix_xor_count[prefix_xor] += 1

    return total


# Test
A = [1, 2, 3, 4, 5]
B = 5
print(count_subarrays_with_xor(A, B))  # Output: 2
