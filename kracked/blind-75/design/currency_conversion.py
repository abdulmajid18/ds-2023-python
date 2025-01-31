from collections import defaultdict


class CurrencyConverter:
    def __init__(self):
        self.graph = defaultdict(dict)

    def add_rate(self, from_currency, to_currency, rate):
        self.graph[from_currency][to_currency] = rate
        self.graph[to_currency][from_currency] = 1 / rate

    def convert(self, amount, from_currency, to_currency):
        if from_currency == to_currency:
            return amount

        visited = set()
        queue = [(from_currency, 1)]

        while queue:
            curr_currency, curr_rate = queue.pop(0)

            if curr_currency == to_currency:
                return amount * curr_rate

            visited.add(curr_currency)

            for next_currency, next_rate in self.graph[curr_currency].items():
                if next_currency not in visited:
                    queue.append((next_currency, curr_rate * next_rate))

        return None  # Conversion not possible


# Example usage
converter = CurrencyConverter()

# Adding conversion rates
converter.add_rate("USD", "EUR", 0.85)
converter.add_rate("EUR", "GBP", 0.88)
converter.add_rate("GBP", "JPY", 150)

# Performing conversions
print(converter.convert(100, "USD", "EUR"))  # Direct conversion
print(converter.convert(100, "USD", "GBP"))  # Indirect conversion
print(converter.convert(100, "USD", "JPY"))  # Multi-step conversion
print(converter.convert(100, "USD", "CAD"))  # Impossible conversion