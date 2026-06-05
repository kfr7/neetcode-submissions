class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = dict()   # at that i, what is the best subsequence after that?

        def helper(i, prev_i = None):
            if i == len(nums):
                return 0

            if (i, prev_i) in memo:
                return memo[(i, prev_i)]
            
            two = 0
            three = 0
            # or we can try adding if we can (if nothing before or if we are gerater than before)
            if prev_i is None or nums[i] > nums[prev_i]:
                two = 1 + helper(i+1, i)
            # either way also call it without adding it
            three = helper(i+1, prev_i)
            result = max(two, three)
            if (i, prev_i) not in memo:
                memo[(i, prev_i)] = result
            memo[(i, prev_i)] = max(memo[(i, prev_i)], result)
            return memo[(i, prev_i)]
        
        return helper(0)
            