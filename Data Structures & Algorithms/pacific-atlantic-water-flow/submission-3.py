
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(i, j, came_from_value, visited):
            if i < 0 or j < 0 or i == len(heights) or j == len(heights[0]) or heights[i][j] < came_from_value:
                return
            if (i, j) in visited:
                return  # we can't visit it again
            visited.add((i, j))
            curr_value = heights[i][j]
            dfs(i+1, j, curr_value, visited)
            dfs(i-1, j, curr_value, visited)
            dfs(i, j+1, curr_value, visited)
            dfs(i, j-1, curr_value, visited)
        
        pacific = set()
        for i in range(len(heights)):
            dfs(i, 0, float('-inf'), pacific)   # left row
        for j in range(len(heights[0])):
            dfs(0, j, float('-inf'), pacific)   # top row
        
        atlantic = set()
        for i in range(len(heights)):
            dfs(i, len(heights[0])-1, float('-inf'), atlantic)  # right row
        for j in range(len(heights[0])):
            dfs(len(heights)-1 ,j, float('-inf'), atlantic) # bottom row
        
        result = []
        for i in range(len(heights)):
            for j in range(len(heights[i])):
                if (i,j) in pacific and (i,j) in atlantic:
                    result.append([i,j])
        return result
         

            
            



        # below works but is not optimal 
        # # memo = dict()   # stores result at a certain grid
        # visited = set()
        # def helper(i, j, came_from_value):   # returns (Bool, Bool)  (Pacific, Atlantic)
        #     if i < 0 or j < 0:
        #         return (True, False)
        #     elif i == len(heights) or j == len(heights[i]):
        #         return (False, True)
        #     # otherwise we are in bounds
        #     curr_value = heights[i][j]
        #     if curr_value > came_from_value:
        #         return (False, False)
        #     # if (i, j) in memo:
        #     #     return memo[(i, j)]
        #     # otherwise, the water can flow in this direction
        #     if (i,j) in visited:
        #         return (False, False)
        #     visited.add((i, j))
        #     one, two = helper(i+1, j, curr_value)
        #     three, four = helper(i-1, j, curr_value)
        #     five, six = helper(i, j+1, curr_value)
        #     seven, eight = helper(i, j-1, curr_value)
        #     visited.remove((i, j))

        #     pacific_reached = one or three or five or seven
        #     atlantic_reached = two or four or six or eight
        #     return (pacific_reached, atlantic_reached)
        #     # return memo[(i,j)]
        # result = []

        # for i in range(len(heights)):
        #     for j in range(len(heights[i])):
        #         pacific_reached, atlantic_reached = helper(i, j, float('inf'))
        #         if pacific_reached and atlantic_reached:
        #             result.append([i, j])
        
        # return result
        