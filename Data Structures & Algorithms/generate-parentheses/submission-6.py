class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 3. IMPLEMENT ITERATIVE SOLUTION TOMORROW (ALL RECURSION CAN USUALLY DONE WITH SMART USE OF STACK) see if you remember in 24 hours
        res = []
        stack = []  # this is equivalent to the recursive call stack so it takes in "arguments"
        # push the base call to it
        # list passed in represents leftRemainder, rightRemainder, building
        stack.append([n, n, ''])
        while len(stack) > 0:
            leftRemainder, rightRemainder, building = stack.pop()
            if leftRemainder == 0 and rightRemainder == 0:
                res.append(building)
                continue
            # otherwise we need to add more stuff to the "call stack"
            if leftRemainder > 0:
                stack.append([leftRemainder - 1, rightRemainder, building + "("])
            if leftRemainder < rightRemainder:
                stack.append([leftRemainder, rightRemainder - 1, building + ")"])
        return res
        # come back sunday night, connect to internet, and see if this works



        # 2. CONVERSED WITH GPT ABOUT LOTS OF LIST CONCATENATION (IMPROVED HERE)
        # def helper(leftRem, rightRem, build):
        #     if leftRem == 0 and rightRem == 0:  # base case
        #         return listSolutions.append(build)

        #     # can always do left side if we have some remaining
        #     if (leftRem > 0):
        #         helper(leftRem-1, rightRem, build + '(')
        #     # we can only do the right side if we have more right than left
        #     if (leftRem < rightRem):
        #         helper(leftRem, rightRem-1, build + ')')
        
        # listSolutions = []
        # helper(n, n, '')
        # return listSolutions

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
                