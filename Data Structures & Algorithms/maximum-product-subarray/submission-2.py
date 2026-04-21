class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        best = max(nums)

        rolling_minimum = 1
        rolling_maximum = 1

        for i in range(len(nums)):
            curr_num = nums[i]
            if curr_num == 0:
                best = max(best, 0)
                rolling_minimum = 1
                rolling_maximum = 1
            else:
                rolling_minimum *= curr_num
                rolling_maximum *= curr_num
                best = max(best, rolling_minimum, rolling_maximum)
                temp = rolling_minimum
                rolling_minimum = min(rolling_maximum, rolling_minimum, curr_num)
                rolling_maximum = max(rolling_maximum, temp, curr_num)
        return best


        # highest = max(nums)
        # rolling_product = 1
        # def dfs(i, rolling_product):
        #     nonlocal highest
        #     if i >= len(nums):
        #         return
        #     curr_num = nums[i]
        #     if curr_num == 0:
        #         highest = max(highest, curr_num)
        #         dfs(i+1, 1) # basically restarting the flow here
        #     else:
        #         # this case avoids having to check division by zero
        #         # then we can either include this number and if not we reset back to 1
        #         rolling_product *= curr_num
        #         highest = max(highest, rolling_product)
        #         dfs(i+1, rolling_product)
        #         dfs(i+1, 1)
        # dfs(0, 1)
        # return highest
