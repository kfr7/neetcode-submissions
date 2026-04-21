class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i in range(len(nums)):
            num = nums[i]
            if num in d:
                return [d[num], i]
            d[target - num] = i
            

            
        