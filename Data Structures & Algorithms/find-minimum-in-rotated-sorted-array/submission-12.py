class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l<=r:
            m = (l+r) // 2
            if (m-1 < 0 and m==r) or nums[m] < nums[m-1]:
                return nums[m]
            elif nums[m] < nums[r]:
                r = m-1
            else:
                l = m+1
        return -1
        