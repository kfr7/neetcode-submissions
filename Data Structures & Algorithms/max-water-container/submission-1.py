class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mostWater = 0
        l, r = 0, len(heights)-1
        while l < r:
            smallestHeight = min(heights[l], heights[r])
            mostWater = max(mostWater, smallestHeight * (r-l))
            if heights[l] == heights[r]:
                # we can move both
                l += 1
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return mostWater
        