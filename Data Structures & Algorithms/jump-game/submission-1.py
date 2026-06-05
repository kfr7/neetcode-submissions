class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # try jumping max, if it does not work, try jumping one less until you hit 0
        def helper(i):
            if i >= len(nums):
                return False
            elif i == len(nums)-1:
                return True
            # otherwise we need to jump still
            for j in range(nums[i], 0, -1):
                if helper(i+j):
                    return True
            return False
        
        return helper(0)