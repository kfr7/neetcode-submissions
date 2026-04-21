class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data = dict()
        # number needed: index that has that number
        for i in range(len(nums)):
            if target - nums[i] in data:
                return [data[target - nums[i]], i]
            data[nums[i]] = i
            





















        # dictionary of {number_needed: index that caused this}
        numbers_needed = dict()
        for i in range(len(nums)):
            if nums[i] in numbers_needed:
                return [numbers_needed[nums[i]], i] # solution guarantees this
            # otherwise add what number is needed for the current number
            numbers_needed[target-nums[i]] = i
    
        