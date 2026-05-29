class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = dict()
        def dfs(i):
            if i >= len(cost):
                return 0

            if i in memo:
                return memo[i]
            
            take_next = dfs(i+1)
            skip_one = dfs(i+2)

            memo[i] = cost[i] + min(take_next, skip_one)

            return memo[i]
        
        return min(dfs(0), dfs(1))


            
        