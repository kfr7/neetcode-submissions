class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 2. CONVERSED WITH GPT ABOUT LOTS OF LIST CONCATENATION (IMPROVED HERE)
        def helper(leftRem, rightRem, build):
            if leftRem == 0 and rightRem == 0:  # base case
                return listSolutions.append(build)

            # can always do left side if we have some remaining
            if (leftRem > 0):
                helper(leftRem-1, rightRem, build + '(')
            # we can only do the right side if we have more right than left
            if (leftRem < rightRem):
                helper(leftRem, rightRem-1, build + ')')
        
        listSolutions = []
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
                