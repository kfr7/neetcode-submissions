class Solution:
    def trap(self, height: List[int]) -> int:
        waterCollected = 0
        # edge case only one height
        if len(height) == 0 or len(height) == 1:
            return waterCollected
        leftIndex, rightIndex = 0, len(height)-1
        leftBarrier, rightBarrier = height[leftIndex], height[rightIndex]
        while leftIndex <= rightIndex:
            # b) but we are limited by the smallest of the two barriers
            if leftBarrier <= rightBarrier:
                tempWaterCollected = leftBarrier - height[leftIndex]
                waterCollected += tempWaterCollected if tempWaterCollected >= 0 else 0
                # a) we always want to take the new tallest barrier
                leftBarrier = max(leftBarrier, height[leftIndex])
                leftIndex += 1
            else:
                tempWaterCollected = rightBarrier - height[rightIndex]
                waterCollected += tempWaterCollected if tempWaterCollected >= 0 else 0
                rightBarrier = max(rightBarrier, height[rightIndex])
                rightIndex -= 1
        return waterCollected





        