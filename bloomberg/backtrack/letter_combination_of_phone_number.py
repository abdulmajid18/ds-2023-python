def letterCombinations(digits):
    if not digits:
        return []

    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }

    result = []

    def backtrack(combination, next_digits):
        if not next_digits:
            result.append(combination)
        else:
            for letter in phone_map[next_digits[0]]:
                backtrack(combination + letter, next_digits[1:])

    backtrack("", digits)
    return result


# Example usage:
combinations = letterCombinations("23")
print(combinations)  # Output: ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
