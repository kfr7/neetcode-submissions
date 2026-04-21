class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        longest_found = 0
        for number in numbers:
            temp_found = 1
            while number + 1 in numbers:
                temp_found += 1
                number += 1
            longest_found = max(longest_found, temp_found)
        
        return longest_found
        
        