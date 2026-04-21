class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tempStack = [temperatures[0]]
        indexStack = [0]
        res = [0 for _ in range(len(temperatures))]

        for i in range(len(temperatures)):
            while len(tempStack) > 0 and temperatures[i] > tempStack[-1]:
                tempStack.pop()
                subtractBy = indexStack.pop()
                res[subtractBy] = i - subtractBy
            # always add to both stacks after while loop
            tempStack.append(temperatures[i])
            indexStack.append(i)
        return res

        