class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []    # will contain everyhing to the left then will contain the result
        leftProduct = 1
        for i in range(len(nums)):
            res.append(leftProduct)
            leftProduct *= nums[i]
        
        # now res has every left product per index
        rightProduct = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= rightProduct
            rightProduct *= nums[i]
        
        return res
            

        