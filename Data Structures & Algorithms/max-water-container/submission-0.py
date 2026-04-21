class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largestArea = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            smallestStick = min(heights[left], heights[right])
            largestArea = max(largestArea, smallestStick * (right-left))
            if heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
                right -= 1
        return largestArea

        