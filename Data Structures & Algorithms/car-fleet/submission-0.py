class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        reverseZipped = sorted([(p, s) for p, s in zip(position, speed)])[::-1]
        for p, s in reverseZipped:
            timeToReachTarget = (target - p) / s
            if len(stack) == 0 or timeToReachTarget > stack[-1]:
                stack.append(timeToReachTarget)
            # otherwise don't add it to the stack
        return len(stack)