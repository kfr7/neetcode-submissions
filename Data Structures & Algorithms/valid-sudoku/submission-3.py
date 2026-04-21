class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        # then the last one can be the row // 3 and col // 3
        sub_squares = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(len(board)):
            for j in range(len(board)):
                character = board[i][j]
                if character == ".":
                    continue
                # otherwise we have a number and we need to see if they are already in the set
                if character in rows[i]:
                    return False
                else:
                    rows[i].add(character)
                
                if character in cols[j]:
                    return False
                else:
                    cols[j].add(character)

                if character in sub_squares[i // 3][j // 3]:
                    return False
                else:
                    sub_squares[i // 3][j // 3].add(character)
        
        return True
    