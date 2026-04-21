class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        known = dict()  # result: index
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in known:
                return [known[diff], i]
            known[nums[i]] = i
        

                    