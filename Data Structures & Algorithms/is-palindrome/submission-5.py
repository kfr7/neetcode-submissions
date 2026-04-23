class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0 or len(s) == 1:
            return True
        
        l, r = 0, len(s)-1
        while l < r:
            do_continue = True
            if not s[l].isalnum():
                l += 1
                do_continue = False
            if not s[r].isalnum():
                r -= 1
                do_continue = False
            if not do_continue:
                continue
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True
        