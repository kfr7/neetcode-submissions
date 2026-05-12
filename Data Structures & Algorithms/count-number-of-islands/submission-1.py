class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def helper(i, j):
            if i < 0 or i == len(grid) or j < 0 or j == len(grid[i]) or grid[i][j] == "0":
                return
            # otherwise just set the i,j
            grid[i][j] = "0"
            helper(i+1,j)
            helper(i-1,j)
            helper(i,j+1)
            helper(i,j-1)
        
        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    num_islands += 1
                    helper(i, j)
        return num_islands

        