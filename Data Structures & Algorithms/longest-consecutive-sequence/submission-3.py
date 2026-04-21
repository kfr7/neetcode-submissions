class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        quickAccess = set(nums)
        if len(nums) == 0:
            return 0
        longest = 1
        for num in nums:
            if num - 1 in quickAccess:
                continue
            else:
                # it is the far left of the sequence
                temp = num + 1
                currCount = 1
                while temp in quickAccess:
                    currCount += 1
                    longest = max(longest, currCount)
                    temp += 1
        return longest
        
        