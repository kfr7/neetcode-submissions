class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        hashmap = set(nums)

        res = 1

        for element in nums:
            if element-1 in hashmap:
                continue    # since we know there is a longer sequence if we start from before
            curr_count = 1
            while element+1 in hashmap:
                curr_count += 1
                element += 1
            res = max(res, curr_count)
        
        return res



        