class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        extra_cell = 1  # needed because cannot treat [0][0] as indicator for BOTH row and cols
        ROWS = len(matrix)
        COLS = len(matrix[0])

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    if i == 0:
                        extra_cell = 0
                    else:
                        matrix[i][0] = 0
                    matrix[0][j] = 0
        # so now within the matrix we correctly flagged which ones along the top row and the left most column
        # iterate through the extra_cell and the 0th column last.
        for k in range(1, ROWS):
            if matrix[k][0] == 0:
                # then we clear this entire row
                for f in range(COLS):
                    matrix[k][f] = 0
        # now go through the columns
        for k in range(COLS):
            if matrix[0][k] == 0:
                # then we can clear this entire column
                for f in range(ROWS):
                    matrix[f][k] = 0
        # now for the extra cell
        if extra_cell == 0:
            # then we clear the 0th row
            for i in range(COLS):
                matrix[0][i] = 0


        # rows = set()
        # cols = set()

        # ROWS = len(matrix)
        # COLS = len(matrix[0])

        # for i in range(ROWS):
        #     for j in range(COLS):
        #         if matrix[i][j] == 0:
        #             rows.add(i)
        #             cols.add(j)
        # for r in rows:  
        #     for j in range(COLS):
        #         matrix[r][j] = 0
        # for c in cols:
        #     for i in range(ROWS):
        #         matrix[i][c] = 0
                