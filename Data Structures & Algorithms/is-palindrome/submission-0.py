class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            moved = False
            if not s[left].isalnum():
                left += 1
                moved = True
            if not s[right].isalnum():
                right -= 1
                moved = True
            # if we didn't move (both alphanumeric) then compare them
            if moved:
                continue
            
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True