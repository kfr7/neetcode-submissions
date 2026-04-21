class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:

            if not (65 <= ord(s[l]) <= 90) and not (97 <= ord(s[l]) <= 122) and not (48 <= ord(s[l]) <= 57):
                l += 1
                continue
            if not (65 <= ord(s[r]) <= 90) and not (97 <= ord(s[r]) <= 122) and not (48 <= ord(s[r]) <= 57):
                r -= 1
                continue        

            if s[l].lower() != s[r].lower():
                return False
            
            # otherwise let's continue
            l += 1
            r -= 1
        
        return True
