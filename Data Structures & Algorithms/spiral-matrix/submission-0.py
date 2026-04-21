class Solution:
    def printMatrix(self, matrix):
        for row in matrix:
            print(row)

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        # set boundaries for the "matrix"
        left, top = 0, 0
        bottom = len(matrix)
        right = len(matrix[0])
        self.printMatrix(matrix)

        while left < right and top < bottom:
            print('left and right:', left, right)
            print('top and bottom:', top, bottom)
            # go right along top border
            for j in range(left, right):
                print('adding matrix[top][j]', matrix[top][j])
                res.append(matrix[top][j])
            # go down along right border
            for i in range(top+1, bottom):
                print('adding matrix[i][right-1]',matrix[i][right-1])
                res.append(matrix[i][right-1])
            # go left along the bottom border if we don't only have 1 row left
            if (bottom - top > 1):
                for j in range(right-2, left-1, -1):
                    print('adding matrix[bottom-1][j]', matrix[bottom-1][j])
                    res.append(matrix[bottom-1][j])
            # go up along the left border but stop before if we don't only have 1 column left
            if (right - left > 1):
                for i in range(bottom-2, top, -1):
                    print('adding matrix[i][left]', matrix[i][left])
                    res.append(matrix[i][left])
            
            # now move all the borders 
            left += 1
            top += 1
            bottom -= 1
            right -= 1
        
        return res


    

        