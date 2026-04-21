from math import ceil, floor

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            number = None
            try:
                number = int(token)
                stack.append(number)
                print(stack)
            except:
                # not a number so pop all the numbers in the stack and perform the operation
                if len(stack) == 0:
                    print('will continue')
                    continue
                else:
                    print('in else with', token)
                    # get the far 2 right numbers
                    right_number = stack.pop()
                    left_number = stack.pop()
                    if token == "+":
                        stack.append(left_number + right_number)
                    elif token == "*":
                        stack.append(left_number * right_number)
                    elif token == "-":
                        stack.append(left_number - right_number)
                    elif token == "/":
                        temp = left_number / right_number
                        if temp > 0:
                            temp = floor(temp)
                        else:
                            temp = ceil(temp)
                        stack.append(temp)
                    print('after computation', stack)

        return stack[0]
            
        