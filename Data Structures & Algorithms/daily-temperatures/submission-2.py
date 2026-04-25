class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # go in reverse order
        stack = []
        result = [None] * len(temperatures)
        for i in range(len(temperatures)-1, -1, -1):
            while len(stack) != 0 and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            temp = temperatures[i]
            if len(stack) == 0:
                result[i] = 0
            else:
                result[i] = stack[-1] - i
            stack.append(i)
        return result