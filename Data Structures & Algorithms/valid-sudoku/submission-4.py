class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(len(board)):
            print(board[i])
        print('------')

        mini_squares = [[set() for _ in range(3)] for _ in range(3)]
        # first rows and cols
        for i in range(len(board)):
            rows_seen = set()
            cols_seen = set()
            for j in range(len(board[i])):
                if board[i][j] != ".":
                    if board[i][j] in rows_seen:
                        return False
                    rows_seen.add(board[i][j])
                    if board[i][j] in mini_squares[i//3][j//3]:
                        return False
                    mini_squares[i//3][j//3].add(board[i][j])
                if board[j][i] != ".":
                    if board[j][i] in cols_seen:
                        return False
                    cols_seen.add(board[j][i])
                
        return True
