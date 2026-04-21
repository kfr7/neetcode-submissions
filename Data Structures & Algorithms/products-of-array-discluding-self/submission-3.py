class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # left pass into temp array then a right pass
        goingRight = []
        for i in range(len(nums)):
            if i == 0:
                goingRight.append(1)
            else:
                goingRight.append(goingRight[-1] * nums[i-1])
        goingLeft = []
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums) - 1:
                goingLeft.append(1)
            else:
                goingLeft.append(goingLeft[-1] * nums[i+1])
        goingLeft = goingLeft[::-1]

        result = []
        for i in range(len(goingLeft)):
            result.append(goingLeft[i] * goingRight[i])
        
        return result
            

        