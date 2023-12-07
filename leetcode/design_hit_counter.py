""" Checkout the binary search Implementation too """

class HitCounter:

    def __init__(self):
        # Initialize two lists to store timestamps and hit counts
        self.timestamps = []
        self.hits = []

    def hit(self, timestamp: int) -> None:
        # Append the current timestamp to the timestamps list
        self.timestamps.append(timestamp)
        # If the list becomes too large, remove old hits
        while timestamp - self.timestamps[0] >= 300:
            self.timestamps.pop(0)
            self.hits.pop(0)
        # Append a new hit or increment the count of the last hit
        if not self.hits or timestamp != self.timestamps[-1]:
            self.hits.append(1)
        else:
            self.hits[-1] += 1

    def getHits(self, timestamp: int) -> int:
        # Calculate the total hits within the last 5 minutes
        total_hits = 0
        for i in range(len(self.timestamps)):
            if timestamp - self.timestamps[i] < 300:
                total_hits += self.hits[i]
            else:
                # Remove old hits
                self.timestamps.pop(0)
                self.hits.pop(0)
        return total_hits
