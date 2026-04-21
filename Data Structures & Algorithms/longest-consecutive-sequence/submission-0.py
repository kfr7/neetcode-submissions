class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # we need all the sequences, so an example [2,20,4,10,3,4,5]
        # would mean 2, 3, 4, 4, 5     10,       20
        numSet = set(nums)
        maxCount = 0
        for num in nums:
            tempNum = num
            tempCount = 1
            # don't start counting the sequence if it isn't the far left number of the sequence
            if tempNum-1 not in numSet:
                while tempNum+1 in numSet:
                    tempNum += 1
                    tempCount += 1
                # when it doesn't find a number to the right it will break
                maxCount = max(maxCount, tempCount)
        return maxCount
        
        