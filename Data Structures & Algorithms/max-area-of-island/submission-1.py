class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def helper(i, j):
            if i < 0 or i == len(grid) or j < 0 or j == len(grid[i]) or grid[i][j] == 0:
                return 0
            
            grid[i][j] = 0
            
            a = helper(i+1, j)
            b = helper(i-1, j)
            c = helper(i, j+1)
            d = helper(i, j-1)

            return 1 + a + b + c + d
        

        area = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    new_answer = helper(i, j)
                    area = max(area, new_answer)
        
        return area


        