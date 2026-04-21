class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, curr_i):
            if i < 0 or j < 0 or i >= ROWS or j >= COLS or board[i][j] != word[curr_i]:
                return False
            # so we know the current letter is good so mark it as "visited"
            temp = board[i][j]
            board[i][j] = "x"
            curr_i += 1
            if (curr_i >= len(word)):
                return True # then we know this was the end of the word

            if (dfs(i+1, j, curr_i) or dfs(i, j+1, curr_i) or dfs(i-1, j, curr_i) or dfs(i, j-1, curr_i)):
                return True
            
            # otherwise we know this letter's future possible paths don't work
            board[i][j] = temp
            return False
        
        if len(word) == 0:
            return True
        if len(board) == 0 or len(board[0]) == 0:
            return False
        
        ROWS = len(board)
        COLS = len(board[0])
        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, 0):
                    return True
        return False


        