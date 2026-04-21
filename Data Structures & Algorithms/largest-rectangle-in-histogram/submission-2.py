class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # it can only get bigger if the ones that are to the right keep going up
        # otherwise you pop the ones that were to the left and move the small one
        # to where the big ones were since the big ones had that area available
        indexStack = []
        heightStack = []
        largestRectangle = 0
        for i in range(len(heights)):
            # if it is empty or the current height is bigger than the top of the stack, append
            if len(heightStack) == 0 or heightStack[-1] < heights[i]:
                heightStack.append(heights[i])
                indexStack.append(i)
            else:
                # the height was either smaller or equal, so pop all the ones
                # that are bigger or equal to it and replace the last index of the one you popped since we want area
                # and the ones we popped technically had that area too
                rightIndex = indexStack[-1]
                tempLowestIndex = None
                while len(heightStack) > 0 and heightStack[-1] >= heights[i]:
                    # this while loop is to compute the largest to smallest to the left of current
                    tempLowestIndex = indexStack.pop()
                    tempHeight = heightStack.pop()
                    largestRectangle = max(largestRectangle, tempHeight * (rightIndex + 1 - tempLowestIndex))

                # now once we exited we can compute the whole distance of the current to the last one we popped
                largestRectangle = max(largestRectangle, heights[i] * (i + 1 - tempLowestIndex))
                # now add it to the stacks with the far left index we popped
                indexStack.append(tempLowestIndex)
                heightStack.append(heights[i])

        # if we have things in the stack, then run algorithm to compare to largestRectangle
        if len(heightStack) > 0:
            rightIndex = indexStack[-1]
            while len(heightStack) > 0:
                poppedHeight = heightStack.pop()
                poppedIndex = indexStack.pop()
                largestRectangle = max(largestRectangle, poppedHeight * (rightIndex + 1 - poppedIndex))
        return largestRectangle


        