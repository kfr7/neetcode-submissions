class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        known = set(nums)
        longest = 0
        for i in range(len(nums)):
            if nums[i]-1 in known:
                continue
            else: # keep on going right
                counter = 1
                curr_num = nums[i]+1
                while curr_num in known:
                    counter += 1
                    curr_num += 1
                longest = max(longest, counter)

        return longest

        