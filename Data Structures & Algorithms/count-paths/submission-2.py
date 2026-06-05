class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = dict()   # store combinations possible at/after this cell
        def dfs(i, j):
            if i < 0 or j < 0 or i == m or j == n:
                return 0
            # other base case is we reached the end
            if i == m-1 and j == n-1:
                return 1
            if (i,j) not in memo:
                memo[(i,j)] = dfs(i+1,j) + dfs(i, j+1)  # then compute both
            return memo[(i,j)]
        return dfs(0,0)
        