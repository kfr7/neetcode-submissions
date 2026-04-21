class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp
        # first index the max is the first index
        # second index the max is between the first index and second index
        # third index is the max of 2 before or (max of 1 before + current)
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)
        
        dp = [nums[0], max(nums[0], nums[1])]

        for i in range(2, len(nums)):
            dp.append(max(nums[i] + dp[i-2], dp[i-1]))
        
        return dp[-1]
        