class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 0 or len(nums) == 1:
            return nums
        # otherwise we will scan torwards the right
        left_side = []
        m = 1
        for i in range(len(nums)):
            if i-1 < 0:
                m = nums[i]
            else:
                left_side.append(m)
                m *= nums[i]
        right_side = [0] * (len(nums)-1)
        m = 1
        for i in range(len(nums)-1, -1, -1):
            if i+1 == len(nums):
                m = nums[i]
            else:
                right_side[i] = m
                m *= nums[i]
        
        print('left:', left_side)
        print('right:', right_side)
        for i in range(len(right_side)):
            if i == 0:
                continue
            right_side[i] = right_side[i] * left_side[i-1]
        right_side.append(left_side[-1])
        return right_side

        
        

        


        