class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # recursively call
        def helper(leftRem, rightRem, build):
            listSolutions = []
            if leftRem == 0 and rightRem == 0:  # base case
                return [build]
            elif (leftRem == rightRem): # must do
                return helper(leftRem-1, rightRem, build + '(')
            elif (leftRem == 0): # must do
                return helper(leftRem, rightRem-1, build + ')')
            else:   # either one is fine
                return helper(leftRem-1, rightRem, build + '(') + helper(leftRem, rightRem-1, build + ')')
        
        return helper(n, n, '')
                