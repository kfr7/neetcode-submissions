class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        mem = [0] * n
        mem[0] = 1  # need base cases
        mem[1] = 2

        for i in range(2, n):
            mem[i] = mem[i-1] + mem[i-2]

        return mem[-1]