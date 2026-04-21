class Solution:
    def isValid(self, s: str) -> bool:
        # STACKS ARE JUST ARRAYS THAT WE PUSH AND POP FROM THE END!!!
        stack = []
        for element in s:
            if element in ('}', ']', ')'):
                if len(stack) == 0:
                    return False
                else:   # pop the last item and see if it matches
                    matching = stack.pop()
                    if element == '}' and matching != '{' \
                        or element == ']' and matching != '[' \
                        or element == ')' and matching != '(':
                        return False
                    # otherwise continue the for loop
            else:
                stack.append(element)
        if len(stack) == 0:
            return True
        return False

        