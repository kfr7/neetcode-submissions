from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)
        for num in nums:
            frequency[num] += 1
        
        arr = [[] for _ in range(len(nums))]
        for key in frequency:
            num = key
            freq_of_num = frequency[key]
            arr[freq_of_num-1].append(num)
                
        result = []
        for i in range(len(arr)-1, -1, -1):            
            for num in arr[i]:
                if len(result) == k:
                    return result
                result.append(num)
        return result

