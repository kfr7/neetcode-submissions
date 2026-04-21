class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        l = [[] for _ in range(len(nums))]
        for key, v in count.items():
            l[v-1].append(key)
        
        answer = []
        for i in range(len(l)-1, -1, -1):
            for element in l[i]:
                answer.append(element)
                print(len(answer), k)
                if len(answer) == k:
                    return answer

