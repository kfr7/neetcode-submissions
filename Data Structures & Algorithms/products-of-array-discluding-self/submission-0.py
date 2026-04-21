class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # you are going to need 2 passes, first go right, then go left
        # can have 2 separate arrays and each index tells you 
        # the product of everything to the left of it (and the second one tells you everything to the right)
        # then loop through both arrays and multiply each matching index together
    
        left_side = []  # no need to hold the 0th index
        left_product = 1
        for i in range(1, len(nums)):
            left_product  *= nums[i-1]
            left_side.append(left_product)

        right_side = [] # no need to hold the last index
        right_product = 1
        for i in range(len(nums) - 2, -1, -1):
            right_product *= nums[i+1]
            right_side.append(right_product)

        right_side = right_side[::-1]
        print(left_side)
        print(right_side)
        
        first_product = right_side[0]
        last_product = left_side[-1]
        right_side.pop(0)
        left_side.pop(-1)
    
        res = [first_product]

        for i in range(len(nums) - 2):
            res.append(left_side[i] * right_side[i])
        
        res.append(last_product)

        return res

        