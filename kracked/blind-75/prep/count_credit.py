from itertools import combinations


def findValidCombinations(participants, credits):
    # Input validation
    if not participants or participants <= 0:
        return 0
    if not credits or not isinstance(credits, list):
        return 0

    MOD = 1000000007
    n = len(credits)

    def isValid(mask):
        # Calculate sum of selected credits
        total = sum(credits[i] for i in range(n) if mask & (1 << i))
        # Check if total is evenly divisible by participants
        return total % participants == 0

    # Use bitmask to generate all possible combinations
    count = 0
    for mask in range(1, 1 << n):  # Start from 1 to exclude empty set
        if isValid(mask):
            count = (count + 1) % MOD

    return count


def print_all_valid_combinations(participants, credits):
    print(f"\nAnalyzing for participants={participants}, credits={credits}")
    n = len(credits)
    valid_combinations = []

    for mask in range(1, 1 << n):
        total = 0
        combination = []
        for i in range(n):
            if mask & (1 << i):
                total += credits[i]
                combination.append(credits[i])

        if total > 0 and total % participants == 0:
            valid_combinations.append((combination, total))
            print(f"Valid combination found: {combination}, sum={total}")

    print(f"Total valid combinations: {len(valid_combinations)}")
    return len(valid_combinations)


# Test both failing cases to understand the issue
participants1, credits1 = 100, [50, 100, 150, 200]
print_all_valid_combinations(participants1, credits1)

participants2, credits2 = 6, [5, 10, 15, 20, 25, 30]
print_all_valid_combinations(participants2, credits2)


def runTests():
    test_cases = [
        (6, [12, 18, 24, 36], 15),
        (1, [1, 2, 3], 7),
        (2, [2, 4, 6], 7),
        (3, [3, 6, 9, 12], 15),
        (7, [2, 4, 6], 0),
        (12, [12, 24, 36, 48, 60], 31),
        (4, [4, 4, 8, 8], 15),
        (0, [1, 2, 3], 0),
        (5, [], 0),
        (100, [50, 100, 150, 200], 15),
        (6, [5, 10, 15, 20, 25, 30], 31)
    ]

    for i, (p, c, expected) in enumerate(test_cases, 1):
        result = findValidCombinations(p, c)
        passed = result == expected
        print(f"Test {i}: {'✓' if passed else '✗'}")
        print(f"  Participants: {p}")
        print(f"  Credits: {c}")
        print(f"  Expected: {expected}, Got: {result}\n")
        if not passed:
            print(f"  Failed test {i}!")
