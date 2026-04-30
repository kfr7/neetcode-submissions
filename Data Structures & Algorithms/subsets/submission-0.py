class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(start, build):
            res.append(build[:])
            for i in range(start, len(nums)):
                build.append(nums[i])
                helper(i+1, build)
                build.pop() # this deals with future iteration not including this number
        helper(0, [])
        return res
