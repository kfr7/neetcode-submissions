class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = dict()

        def dfs(remaining):
            if remaining < 0:
                return float('inf')
            if remaining == 0:
                return 0
            
            if remaining in memo:
                return memo[remaining]
            
            # otherwise lets try the rest of the coins
            best = float('inf')
            for coin in coins:
                best = min(
                    best,
                    1 + dfs(remaining-coin)
                )
            
            memo[remaining] = best
            return memo[remaining]
        
        response = dfs(amount)
        if response == float('inf'):
            return -1
        return response
        