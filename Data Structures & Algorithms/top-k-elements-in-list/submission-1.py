class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get all the counts then map them to an array of len(nums) and go backwards
        counts = dict()
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        groupedCounts = [[] for _ in range(len(nums))]
        # index i is equal to the count - 1
        for key, value in counts.items():
            groupedCounts[value-1].append(key)

        res = []
        for i in range(len(groupedCounts) - 1, -1, -1):
            for element in groupedCounts[i]:
                res.append(element)
                if len(res) == k:
                    return res
