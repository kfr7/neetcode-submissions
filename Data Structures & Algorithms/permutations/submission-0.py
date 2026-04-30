class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(visited, build):
            if len(visited) == len(nums):
                res.append(build[:])
            for num in nums:
                if num not in visited:
                    visited.add(num)
                    build.append(num)
                    helper(visited, build)
                    visited.remove(num)
                    build.pop()
                # else we just skip over it
        helper(set(), [])
        return res
        