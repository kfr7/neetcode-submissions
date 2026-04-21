class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        found = set()
        for n in nums:
            if n in found:
                return True
            found.add(n)
        return False