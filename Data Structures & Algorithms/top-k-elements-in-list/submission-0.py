class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we first need a dictionary to count each number
        # then we can create an array that is one bigger than the array
        # that was passed in and use the indexes and the counts
        # and the values are lists of numbers that had that count
        # then go through the array backwards O(n)
        countDict = dict()
        for num in nums:
            countDict[num] = 1 + countDict.get(num, 0)
        
        # + 1 because we are starting from 0 which is kind of useless but for readibility
        countArray = [[] for i in range(len(nums) + 1)]
        for num, count in countDict.items():
            countArray[count].append(num)
        
        res = []
        for i in range(len(countArray) - 1, 0, -1):
            for num in countArray[i]:
                res.append(num)
                if (len(res) == k):
                    return res
        