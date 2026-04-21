class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1 for _ in range(amount+1)]

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

        # above is the top down dfs
        # but you can also use dp table with bottom up
        # dp = [0]
        # for i in range(1, amount+1):
        #     dp.append(float('inf'))
        #     for coin in coins:
        #         if i - coin < 0:
        #             # then we went over the value so this won't help
        #             pass
        #         else:   # we can use this coin so se
        #             dp[-1] = min(dp[-1], 1 + dp[i - coin])
        # if dp[-1] == float('inf'):
        #     return -1
        # return dp[-1]