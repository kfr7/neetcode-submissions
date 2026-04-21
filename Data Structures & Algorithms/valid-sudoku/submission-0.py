class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        squares = dict()    # keys are 
        # square is:
        # (0, 0), (0, 1), (0, 2)
        # (1, 0), (1, 1), (1, 2)
        # (2, 0), (2, 1), (2, 2)

        for i in range(9): # per row
            for j in range(9): # per column
                # skip if empty
                if board[i][j] == ".":
                    # print("continuing")
                    continue
                # check if the number already exists in that row
                # print('on the number of', board[i][j])
                if board[i][j] in rows[i] or board[i][j] in columns[j] or board[i][j] in squares.get(tuple((i // 3, j // 3)), set()):
                    return False

                # otherwise add it to each set
                # print('rows before:', rows)
                # print(rows[i])
                rows[i].add(board[i][j])
                # print('rows after:', rows)

                columns[j].add(board[i][j])
                existing_set = squares.get(tuple((i // 3, j // 3)), set())
                existing_set.add(board[i][j])
                squares[tuple((i // 3, j // 3))] = existing_set
        return True
                
        