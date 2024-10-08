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
