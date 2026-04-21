class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1. THIS SOLUTION IS ME BEFORE LOOKING IT UP TRYING TO MAKE IT BETTER
        # a = [1, 2, 4, 6]
        # b = [1, 1, 1, 1]    # first holds all left values, but will then mutate the top one
        # first pass results in
        # b = [1, 1, 2, 8]
        # then on the way store the far right variable as the new product, and replace it
        # temp a[i] then...
        # right_product * b[i] is stored in a[i]
        # but then right_product *= a[i]

        # a = [1, 2, 4, 8] at i = 2, store 4, replace 4 with 6 * 2, right_product = 6 * 4
        # a = [1, 2, 12, 8] at i = 1, store 2, replace 2 with 24 * 1, right_product = 24 * 2
        # a = [1, 24, 12, 8] at i = 0, replace 1 with 48 * 1
        # a = [48, 24, 12, 8]

        a = nums
        b = [1 for i in range(len(nums))]

        left_product = 1
        for i in range(1, len(a)):
            left_product *= a[i-1]
            b[i] = left_product
        
        # now that we reached the end go backwards but mutate a instead
        # multiply the stored value that was on the right by the value of the index of b
        right_product = a[-1]
        a[-1] = b[-1]
        for i in range(len(nums)-2, -1, -1):    # go backwards but skip the last index
            temp = a[i]
            a[i] = right_product * b[i]
            right_product *= temp

        return a
        


        # 1. BELOW IS MY FIRST SOLUTION WITHOUT NEETCODE
        # you are going to need 2 passes, first go right, then go left
        # can have 2 separate arrays and each index tells you 
        # the product of everything to the left of it (and the second one tells you everything to the right)
        # then loop through both arrays and multiply each matching index together
    
        # left_side = []  # no need to hold the 0th index
        # left_product = 1
        # for i in range(1, len(nums)):
        #     left_product  *= nums[i-1]
        #     left_side.append(left_product)

        # right_side = [] # no need to hold the last index
        # right_product = 1
        # for i in range(len(nums) - 2, -1, -1):
        #     right_product *= nums[i+1]
        #     right_side.append(right_product)

        # right_side = right_side[::-1]
        
        # first_product = right_side[0]
        # last_product = left_side[-1]
        # right_side.pop(0)
        # left_side.pop(-1)
    
        # res = [first_product]

        # for i in range(len(nums) - 2):
        #     res.append(left_side[i] * right_side[i])
        
        # res.append(last_product)

        # return res

        