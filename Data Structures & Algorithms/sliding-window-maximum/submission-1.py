class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, k-1
        res = []
        while r < len(nums):
            # print(l, r)
            res.append(max([nums[k] for k in range(l, r+1)]))
            l += 1
            r += 1
        return res
        