class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited = set()
        for element in nums:
            if element in visited:
                return True
            visited.add(element)
        return False
         