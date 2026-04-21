class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        store = [[] for _ in range(len(nums)+1)]

        for key, value in count.items():
            store[value].append(key)
        
        result = []
        for i in range(len(store)-1, -1, -1):
            for element in store[i]:
                result.append(element)
                if len(result) == k:
                    return result


