class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch not in ['(', ')', '{', '}', '[', ']']:
                return False
            if ch in ['(', '{', '[']:
                stack.append(ch)
            else:
                if len(stack) == 0: 
                    return False
                last = stack.pop()
                if ch == ')' and last != '(':
                    return False
                if ch == '}' and last != '{':
                    return False
                if ch == ']' and last != '[':
                    return False
        return len(stack) == 0
                    
            

        