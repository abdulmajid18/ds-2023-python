from collections import deque

def findTheWinner(n, k):
    # Initialize a queue with numbers from 1 to n
    queue = deque(range(1, n + 1))

    while len(queue) > 1:
        # Eliminate the k-th person
        for _ in range(k - 1):
            queue.append(queue.popleft())
        queue.popleft()

    # The last remaining person is the winner
    return queue[0]

# Example usage:
n = 5
k = 2
winner = findTheWinner(n, k)
print("The winner is:", winner)  # Output: The winner is: 3
