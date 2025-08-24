class Solution:
    def findNthDigit(self, n: int) -> int:
        digit_length = 1
        count = 9
        start = 1

        while n > digit_length * count:
            n -= digit_length * count
            digit_length += 1
            count *= 10
            start *= 10

        num = start + (n - 1) // digit_length

        digit_index = (n - 1) % digit_length
        return int(str(num)[digit_index])


s = "12345678910111213141516..."