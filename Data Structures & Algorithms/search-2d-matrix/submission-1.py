class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        while l <= r:
            mid = (l + r) // 2
            tempNum = matrix[mid][0]
            if tempNum == target: # edge case
                return True
            if tempNum > target:    # then go up a row
                r = mid - 1
            elif (mid != len(matrix) - 1 and matrix[mid+1][0] > target) or mid == len(matrix) - 1:
                # then enter and do binary search
                l = 0
                r = len(matrix[mid]) - 1
                while l <= r:
                    innerMid = (l + r) // 2
                    if matrix[mid][innerMid] == target:
                        return True
                    elif matrix[mid][innerMid] > target:
                        r = innerMid - 1
                    else:
                        l = innerMid + 1

            else:   # then go down a row
                l = mid + 1
        
        return False
        