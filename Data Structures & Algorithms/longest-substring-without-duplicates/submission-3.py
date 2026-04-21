class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, maximum = 0, 0, 0
        found = set()
        while right < len(s):
            print(found)
            if s[right] in found:
                while s[right] in found:
                    found.remove(s[left])
                    left += 1
                found.add(s[right])
            else:
                found.add(s[right])
                maximum = max(maximum, len(found))
            right += 1 
        return maximum
        