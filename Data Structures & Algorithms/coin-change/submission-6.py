class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0]
        for i in range(amount):
            dp.append(-1)

        def dfs(amountLeft):
            if amountLeft < 0:  # we added too much
                return float('inf') # since we just the minimum
            elif amountLeft == 0: # then we are done
                return 0
            elif amountLeft > 0:
                # then we have more coins to try still
                if dp[amountLeft] != -1:    
                    # if we already calculated this
                    return dp[amountLeft]
                else:   # we need to see which coin is the best
                    smallest_amount = float('inf')
                    for coin in coins:
                        smallest_amount = min(smallest_amount, dfs(amountLeft-coin))
                    # we used 1 coin in this iteration + however many minimum
                    if smallest_amount == float('inf'):
                        # then no coins worked
                        dp[amountLeft] = float('inf')
                    else:
                        dp[amountLeft] = 1 + smallest_amount
                    return dp[amountLeft]
        result = dfs(amount)
        if result == float('inf'):
            return -1
        return result






        