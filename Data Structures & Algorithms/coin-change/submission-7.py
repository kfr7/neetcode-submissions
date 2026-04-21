class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # that was the top down dfs
        # but you can also use dp table with bottom up
        dp = [0]
        for i in range(1, amount+1):
            dp.append(float('inf'))
            for coin in coins:
                if i - coin < 0:
                    # then we went over the value so this won't help
                    pass
                else:   # we can use this coin so se
                    dp[-1] = min(dp[-1], 1 + dp[i - coin])
        if dp[-1] == float('inf'):
            return -1
        return dp[-1]