class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        found_already = set()
        for num in nums:
            if num in found_already:
                return True
            found_already.add(num)
        return False