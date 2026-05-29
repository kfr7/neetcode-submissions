class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]

        def helper(houses):
            if len(houses) == 0:
                return 0
            elif len(houses) == 1:
                return houses[0]
            # otherwise we have logic to do
            back2 = houses[0]
            back1 = max(houses[0], houses[1])
            for i in range(2, len(houses)):
                rob_it = houses[i] + back2
                dont = back1

                best_decision = max(rob_it, dont)

                back2 = back1
                back1 = best_decision
            
            return back1
        
        return max(helper(nums[1:]), helper(nums[:-1]))
        