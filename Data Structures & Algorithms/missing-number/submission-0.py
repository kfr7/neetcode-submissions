class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        one = 0
        two = 0
        for i in range(len(nums)+1):
            one += i
            if i < len(nums):
                two += nums[i]
        return one - two
        
        

        