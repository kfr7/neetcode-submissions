class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0
        while i <= len(nums) - 3:
            print("i outside is:", i)
            while i != 0 and i < len(nums) and nums[i] == nums[i-1]:
                i += 1
            if i == len(nums):
                break
            # the current number is our target, remember that
            # and with our current number, keep going while l <= r because may be more than one triplet w/
            # this number but we won't get it if we stop at first result with this target
            l, r = i+1, len(nums)-1
            while l < r:
                print("lr:", l, r)
                total = nums[i] + nums[l] + nums[r]
                if total > 0: 
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    # then it is equal to it
                    res.append([nums[i], nums[l], nums[r]])
                    # now go to the next number
                    while l < len(nums) - 2 and nums[l] == nums[l+1]:
                        l += 1   
                    l += 1
            i += 1     
        return res                