class Solution:
    def findMin(self, nums: List[int]) -> int:
        # the minimum has a number greater than it to the left. that is our return condition
        # use the r value to check if it is smaller than mid
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l+r) // 2
            # case where we are at the minimum
            if ((mid == 0 and nums[len(nums) - 1] > nums[mid]) or (mid != 0 and nums[mid-1] > nums[mid]) or len(nums) == 1):
                return nums[mid]
            elif nums[mid] > nums[len(nums) - 1]:
                l = mid + 1
            else:
                r = mid - 1
