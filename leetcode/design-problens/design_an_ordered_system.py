from typing import List


class OrderedStream:

    def __init__(self, n: int):
        self.stream = [None] * n  # Initialize an array to store values
        self.ptr = 0  # Pointer to the last inserted value
        self.n = n  # Total number of values

    def insert(self, idKey: int, value: str) -> List[str]:
        # Convert 1-based index to 0-based index
        idKey -= 1
        self.stream[idKey] = value  # Insert the value into the stream
        result = []

        # Check if the newly inserted value can create a chunk
        while self.ptr < self.n and self.stream[self.ptr] is not None:
            result.append(self.stream[self.ptr])
            self.ptr += 1

        return result
