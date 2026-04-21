class Solution:
    def rob(self, nums: List[int]) -> int:
        # we either do pretend to include the first house and we don't include the last house, or vice versa
        def helper(exclude = 'first'):
            dp = []
            start = 2
            end = len(nums)-1
            if exclude == 'first':
                dp.append(nums[1])
                dp.append(max(nums[1], nums[2]))
                start = 3
                end = len(nums)
            else:
                dp.append(nums[0])
                dp.append(max(nums[0], nums[1]))
            
            print('exclude and dp is:', exclude, dp)

            for i in range(start, end):
                dp.append(max(nums[i]+dp[-2], dp[-1]))
            
            return dp[-1]
            

        

        if len(nums) == 0:
            return 0
        if len(nums) <= 3:
            return max(nums)
        
        return max(helper('last'), helper('first'))
        