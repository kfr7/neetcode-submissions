class Trie:
    def __init__(self):
        self.t = dict()
    
    def add(self, word):
        curr = self.t
        for i in range(len(word)):
            letter = word[i]
            if letter not in curr:
                curr[letter] = dict()
            # otherwise it is already there
            if i == len(word)-1:
                curr[letter]["end"] = True
            else:
                curr = curr[letter]

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # first create a trie for the known words
        trie = Trie()
        for word in words:
            trie.add(word)

        res, visited = set(), set()
                
        ROWS = len(board)
        COLS = len(board[0])
        def dfs(r, c, node, word):
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] not in node or ((r,c) in visited):
                return
            # otherwise we have a chance
            visited.add((r,c))
            word += board[r][c]
            node = node[board[r][c]]
            if "end" in node:
                res.add(word)
            
            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)
            visited.remove((r,c))

        for i in range(len(board)):
            for j in range(len(board[i])):
                dfs(i, j, trie.t, '')
        return list(res)





        