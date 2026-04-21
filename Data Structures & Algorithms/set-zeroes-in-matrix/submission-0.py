class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = set()
        cols = set()

        ROWS = len(matrix)
        COLS = len(matrix[0])

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        for r in rows:  
            for j in range(COLS):
                matrix[r][j] = 0
        for c in cols:
            for i in range(ROWS):
                matrix[i][c] = 0
                