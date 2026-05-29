class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        back2 = nums[0]
        back1 = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            # we can either rob this house
            rob_this = nums[i] + back2
            skip_this = back1

            curr = max(skip_this, rob_this)
            back2 = back1
            back1 = curr
        
        return back1
        
        