from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we can have an array and each element is another array
        frequencyMap = [[] for _ in range(len(nums))]
        frequencyDict = defaultdict(int)

        for number in nums:
            frequencyDict[number] += 1
        
        for key, val in frequencyDict.items():
            frequencyMap[val-1].append(key)
        
        # then loop through the freuqncy map backwards
        result = []
        for i in range(len(frequencyMap)-1, -1, -1):
            for element in frequencyMap[i]:
                result.append(element)
                if len(result) == k:
                    return result
        return result
            
        