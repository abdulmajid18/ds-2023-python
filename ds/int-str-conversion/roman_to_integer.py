def roman_to_int(s):
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    result = 0

    for i in range(len(s)):
        current_symbol = s[i]
        current_value = roman_values[current_symbol]

        if i + 1 < len(s) and current_value < roman_values[s[i + 1]]:
            result -= current_value
        else:
            result += current_value

    return result


# Example usage
roman_numeral = "IX"
result = roman_to_int(roman_numeral)
print(f"The integer value of {roman_numeral} is: {result}")
