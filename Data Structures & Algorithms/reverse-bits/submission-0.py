class Solution:
    def reverseBits(self, n: int) -> int:
        new_number = 0
        for i in range(32):
            # first get the far right value of n
            inserting = n & 1
            new_number = new_number << 1
            new_number |= inserting
            n = n >> 1
        return new_number

        