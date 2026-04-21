class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # curr_product coming from left
        # [*, 1, 2, 8]
        # curr_product coming from right
        # [48, 24 , 6, *]

        left_array = [1]
        curr_product = 1
        for i in range(1, len(nums)):
            curr_product *= nums[i-1]
            left_array.append(curr_product)
                
        curr_product = 1
        for j in range(len(nums)-1, -1, -1):
            if (j == (len(nums) - 1)):
                previous_number = nums[j]
                nums[j] = left_array[j]
            else:
                curr_product *= previous_number
                previous_number = nums[j]
                nums[j] = curr_product * left_array[j]

        return nums
        
    
        
        # reverse the right_array for readbility
        right_array = right_array[::-1]
        result_array = []
        for i in range(len(left_array)):
            result_array.append(left_array[i] * right_array[i])
        
        return result_array
