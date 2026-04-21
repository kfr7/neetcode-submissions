class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # every sequence must have a beginning, therefore
        # if we create a set out of the list then we have O(1) lookup
        # to the left of each number as we loop through the nums
        # if it is the farmost left number,then we can keep on checking
        # the far right number
        largest = 0
        setOfNums = set(nums)
        for i in range(len(nums)):
            if nums[i]-1 in setOfNums:
                continue
            # else this is the far left number so keep going right
            count = 1
            tempNum = nums[i]
            while tempNum+1 in setOfNums:
                count += 1
                tempNum += 1
            largest = max(largest, count)
        return largest
        