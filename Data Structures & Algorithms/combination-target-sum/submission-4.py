class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def helper(start, build, curr_rolling_sum):
            if start == len(nums):
                return
            # otherwise continue
            for i in range(start, len(nums)):
                if nums[i] + curr_rolling_sum > target:
                    continue # we know it won't work
                elif nums[i] + curr_rolling_sum == target:
                    build.append(nums[i])
                    res.append(build[:])
                    build.pop()
                    # helper(i+1, build, curr_rolling_sum) 
                else:   # we are still less than so go ahead and add to build (or skip)
                    build.append(nums[i])
                    curr_rolling_sum += nums[i]
                    # helper(i+1, build, curr_rolling_sum)    # do one without duplicating
                    helper(i, build, curr_rolling_sum)  # since we can resuse it too
                    build.pop()
                    curr_rolling_sum -= nums[i]
        helper(0, [], 0)
        return res

        