class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first find the row it belongs to, at each mid row, see if the number is between [0] and [-1] indexes
        l, r = 0, len(matrix) - 1
        while l <= r:
            m = (r+l) // 2
            if matrix[m][0] <= target <= matrix[m][-1]:
                #now we have inner binary search
                l2, r2 = 0, len(matrix[m])-1
                while l2 <= r2:
                    m2 = (l2+r2) // 2
                    print('l2 r2 m2', l2, r2, m2)
                    if matrix[m][m2] == target:
                        return True
                    elif matrix[m][m2] > target:
                        r2 = m2-1
                    else:
                        l2 = m2+1
                return False
            elif target < matrix[m][0]:
                r = m-1
            else:
                l = m+1
        return False
        