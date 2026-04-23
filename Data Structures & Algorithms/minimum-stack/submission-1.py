class MinStack:

    def __init__(self):
        self.min_at_point = []
        self.actual_stack = []
        

    def push(self, val: int) -> None:
        self.actual_stack.append(val)
        if len(self.min_at_point) != 0:
            self.min_at_point.append(min(self.min_at_point[-1], val))
        else:
            self.min_at_point.append(val)
        
    def pop(self) -> None:
        self.min_at_point.pop()
        return self.actual_stack.pop()
        

    def top(self) -> int:
        return self.actual_stack[-1]
        

    def getMin(self) -> int:
        return self.min_at_point[-1]
        
