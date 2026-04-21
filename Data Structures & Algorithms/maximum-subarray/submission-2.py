class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currCount = 0
        maxCount = float('-inf')
        l, r = 0, 0

        while r < len(nums):
            currCount += nums[r]
            maxCount = max(maxCount, currCount)
            # print(l, r, nums[r], currCount, maxCount)
            r += 1
            if currCount < 0:
                currCount = 0
                l = r

        return maxCount




        