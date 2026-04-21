class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 2. BELOW IS CHAT GPT'S IMPROVED VERSIO ( just better squares since it isn't a dictionary )
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]
        # squares indexes related to each square's numbers:
        # 0, 1, 2
        # 3, 4, 5
        # 6, 7, 8

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if (board[i][j] in rows[i] or 
                    board[i][j] in columns[j] or 
                    board[i][j] in squares[(i // 3) * 3 + j // 3]):
                    return False

                rows[i].add(board[i][j])
                columns[j].add(board[i][j])
                squares[(i // 3) * 3 + j // 3].add(board[i][j])

        return True




        # 1. BELOW IS MY ATTEMPT
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        squares = dict()
        # square's keys are:
        # (0, 0), (0, 1), (0, 2)
        # (1, 0), (1, 1), (1, 2)
        # (2, 0), (2, 1), (2, 2)

        for i in range(9): # per row
            for j in range(9): # per column
                # skip if empty
                if board[i][j] == ".":
                    continue
                # check if the number already exists in that row/column/square
                if board[i][j] in rows[i] or board[i][j] in columns[j] or board[i][j] in squares.get(tuple((i // 3, j // 3)), set()):
                    return False

                # otherwise add it to each set
                rows[i].add(board[i][j])
                columns[j].add(board[i][j])
                existing_set = squares.get(tuple((i // 3, j // 3)), set())
                existing_set.add(board[i][j])
                squares[tuple((i // 3, j // 3))] = existing_set
        return True
                
        