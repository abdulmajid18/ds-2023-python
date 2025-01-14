from collections import Counter
from math import gcd
from functools import reduce


def balanceContent(content):
    # Step 1: Count the frequency of each character
    freq = Counter(content)

    # Step 2: Calculate the GCD of all frequencies
    freq_values = list(freq.values())
    if len(freq_values) == 1:
        return 0  # All characters are already balanced.

    overall_gcd = reduce(gcd, freq_values)

    # Step 3: Calculate the minimum number of operations to balance frequencies
    total_operations = 0
    for count in freq_values:
        # To make all characters have the same frequency as the GCD:
        total_operations += abs(count - overall_gcd)

    return total_operations


# Example usage:
content = "xzyxza"
result = balanceContent(content)
print(f"Minimum operations to balance content: {result}")
