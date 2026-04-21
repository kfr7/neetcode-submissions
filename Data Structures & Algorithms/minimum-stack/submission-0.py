class MinStack:

    def __init__(self):
        self.actualStack = []
        self.currentMinimum = []
        

    def push(self, val: int) -> None:
        self.actualStack.append(val)
        if len(self.currentMinimum) == 0 or self.currentMinimum[-1] > val:
            self.currentMinimum.append(val)
        else:
            self.currentMinimum.append(self.currentMinimum[-1])

    def pop(self) -> None:
        self.actualStack.pop()
        self.currentMinimum.pop()
        
    def top(self) -> int:
        return self.actualStack[-1]

    def getMin(self) -> int:
        return self.currentMinimum[-1]
        
