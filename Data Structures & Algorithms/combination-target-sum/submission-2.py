class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # so we can either include this number or not, we don't have to sort the distinct integers
        # but we need some boundary
        res = []
        build = []
        def dfs(i, curr_sum):
            if curr_sum == target:
                res.append(build[::])
            elif i >= len(nums):
                pass
            elif curr_sum < target: # then we can continue adding to the build array
                # first case we include the number we are currently at
                curr_sum += nums[i]
                build.append(nums[i])
                dfs(i, curr_sum)
                # now we can see if we don't include it if we will be fine
                curr_sum -= nums[i]
                build.pop()
                dfs(i+1, curr_sum)
            else:   # we went over so no need to continue doing anything
                pass
        
        dfs(0, 0)
        return res
            
        