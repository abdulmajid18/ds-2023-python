class Bitset:
    def __init__(self, size):
        """
        Initializes the Bitset with 'size' bits, all set to 0.

        :param size: The number of bits in the Bitset.
        """
        self.size = size
        self.bits = [0] * size

    def fix(self, idx):
        """
        Updates the value of the bit at the given index to 1 if it's currently 0.

        :param idx: The index of the bit to fix.
        """
        if 0 <= idx < self.size:
            self.bits[idx] = 1

    def unfix(self, idx):
        """
        Updates the value of the bit at the given index to 0 if it's currently 1.

        :param idx: The index of the bit to unfix.
        """
        if 0 <= idx < self.size:
            self.bits[idx] = 0

    def flip(self):
        """
        Flips the values of all bits in the Bitset.
        """
        for i in range(self.size):
            self.bits[i] = 1 - self.bits[i]

    def all(self):
        """
        Checks if all bits in the Bitset are set to 1.

        :return: True if all bits are 1, False otherwise.
        """
        return all(bit == 1 for bit in self.bits)

    def one(self):
        """
        Checks if there is at least one bit in the Bitset set to 1.

        :return: True if at least one bit is 1, False otherwise.
        """
        return any(bit == 1 for bit in self.bits)

    def count(self):
        """
        Returns the total number of bits in the Bitset set to 1.

        :return: The count of bits set to 1.
        """
        return sum(1 for bit in self.bits if bit == 1)

    def __str__(self):
        """
        Returns a string representation of the current composition of the Bitset.

        :return: A string of '0's and '1's representing the Bitset.
        """
        return ''.join(map(str, self.bits))


# Example usage:
if __name__ == "__main__":
    bitset = Bitset(8)
    bitset.fix(2)
    bitset.fix(5)
    bitset.flip()
    print(bitset)  # Output: '10101010'
    print(bitset.all())  # Output: False
    print(bitset.one())  # Output: True
    print(bitset.count())  # Output: 4
