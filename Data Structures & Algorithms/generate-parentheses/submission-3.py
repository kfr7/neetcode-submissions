class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 2. CONVERSED WITH GPT ABOUT LOTS OF LIST CONCATENATION (IMPROVED HERE)
        listSolutions = []
        def helper(leftRem, rightRem, build):
            if leftRem == 0 and rightRem == 0:  # base case
                return listSolutions.append(build)
            elif (leftRem == rightRem): # must do
                helper(leftRem-1, rightRem, build + '(')
            elif (leftRem == 0): # must do
                helper(leftRem, rightRem-1, build + ')')
            else:   # either one is fine
                helper(leftRem-1, rightRem, build + '(')
                helper(leftRem, rightRem-1, build + ')')
        
        helper(n, n, '')
        return listSolutions

        # 1. FIRST ATTEMPT
        # recursively call
        # def helper(leftRem, rightRem, build):
        #     listSolutions = []
        #     if leftRem == 0 and rightRem == 0:  # base case
        #         return [build]
        #     elif (leftRem == rightRem): # must do
        #         return helper(leftRem-1, rightRem, build + '(')
        #     elif (leftRem == 0): # must do
        #         return helper(leftRem, rightRem-1, build + ')')
        #     else:   # either one is fine
        #         return helper(leftRem-1, rightRem, build + '(') + helper(leftRem, rightRem-1, build + ')')
        
        # return helper(n, n, '')
                