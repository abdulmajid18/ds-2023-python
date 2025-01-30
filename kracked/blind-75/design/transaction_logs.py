import datetime
from collections import defaultdict


class Transaction:
    def __init__(self, user_id, amount, timestamp, location):
        self.user_id = user_id
        self.amount = amount
        self.timestamp = datetime.datetime.fromisoformat(timestamp)
        self.location = location


class TransactionAnalyzer:
    def __init__(self):
        self.transactions = []
        self.user_transactions = defaultdict(list)

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        self.user_transactions[transaction.user_id].append(transaction)

    def analyze_transactions(self):
        alerts = []

        for user_id, user_txns in self.user_transactions.items():
            # Sort transactions by timestamp
            user_txns.sort(key=lambda t: t.timestamp)

            # Check for frequent large transactions
            large_txn_count = sum(1 for t in user_txns if t.amount > 1000)
            if large_txn_count >= 3:
                alerts.append(f"Alert: User {user_id} has {large_txn_count} large transactions")

            # Check for transactions in different locations within a short time
            for i in range(len(user_txns) - 1):
                time_diff = user_txns[i + 1].timestamp - user_txns[i].timestamp
                if time_diff <= datetime.timedelta(hours=1) and user_txns[i].location != user_txns[i + 1].location:
                    alerts.append(f"Alert: User {user_id} has transactions in different locations within 1 hour")
                    break

            # Check for frequent transactions (within a minute of each other)
            for i in range(len(user_txns) - 1):
                time_diff = user_txns[i + 1].timestamp - user_txns[i].timestamp
                if time_diff <= datetime.timedelta(minutes=1):
                    alerts.append(f"Alert: User {user_id} has transactions occurring within a minute of each other")
                    break

        return alerts


# Example usage
analyzer = TransactionAnalyzer()

# Add sample transactions
transactions = [
    Transaction("user1", 500, "2024-03-01T10:00:00", "New York"),
    Transaction("user1", 1500, "2024-03-01T11:30:00", "Los Angeles"),
    Transaction("user1", 2000, "2024-03-01T12:00:00", "Chicago"),
    Transaction("user2", 100, "2024-03-01T09:00:00", "Miami"),
    Transaction("user2", 200, "2024-03-01T09:00:30", "Miami"),  # 30 seconds after previous transaction
    Transaction("user2", 3000, "2024-03-01T10:00:00", "Miami"),
    Transaction("user3", 50, "2024-03-01T14:00:00", "Boston"),
    Transaction("user3", 75, "2024-03-01T14:00:45", "Boston"),  # 45 seconds after previous transaction
    Transaction("user3", 100, "2024-03-01T14:01:30", "Boston"),
]

for txn in transactions:
    analyzer.add_transaction(txn)

# Analyze transactions and print alerts
alerts = analyzer.analyze_transactions()
for alert in alerts:
    print(alert)

import datetime
from collections import defaultdict

# ... [Previous Transaction and TransactionAnalyzer class definitions remain the same] ...

# Time and Space Complexity Analysis

"""
Time Complexity Analysis:

1. add_transaction method:
   - Time Complexity: O(1)
   - This method performs constant time operations: appending to a list and adding to a defaultdict.

2. analyze_transactions method:
   - Time Complexity: O(n log n), where n is the total number of transactions
   - Breaking it down:
     a. Sorting transactions for each user: O(m log m), where m is the number of transactions per user
     b. Iterating through sorted transactions: O(m)
     c. Worst case (all transactions belong to one user): O(n log n)
   - The method performs these operations for each user, but the total number of transactions processed remains n

Space Complexity Analysis:

1. Overall space complexity: O(n), where n is the total number of transactions
   - self.transactions list: O(n)
   - self.user_transactions defaultdict: O(n)
   - The space used by individual Transaction objects: O(n)

2. Additional space in analyze_transactions:
   - alerts list: O(k), where k is the number of alerts generated (worst case O(n))
   - Temporary variables and loop counters: O(1)

Optimization Considerations:

1. If the transactions are already sorted by timestamp when received, we could eliminate the sorting step,
   reducing the time complexity to O(n).

2. For very large datasets, we might consider processing transactions in batches or implementing a sliding
   window approach to limit memory usage.

3. If we need to query user transactions frequently, we could consider using a more sophisticated data 
   structure like a balanced tree for each user's transactions, allowing for O(log m) insertion and 
   range query times.

Trade-offs:

- The current implementation prioritizes simplicity and readability over absolute performance.
- For small to medium-sized datasets, this implementation should perform adequately.
- For very large datasets or high-frequency transaction systems, more advanced data structures and 
  algorithms might be necessary, potentially sacrificing some readability for performance.
"""

# Example usage remains the same...