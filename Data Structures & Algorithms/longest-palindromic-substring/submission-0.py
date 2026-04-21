class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return 0

        best = 1
        best_l, best_r = 0, 1
        for i in range(len(s)):
            # first do it with a center
            l, r = i, i
            while (l == r) or (l >= 0 and r < len(s) and s[l].lower() == s[r].lower()):
                l -= 1
                r += 1
            
            if r-l-1 > best:
                best = r-l-1
                best_l = l+1
                best_r = r

            # then if it is not the first letter, do it for letters that are adjacent that are the same
            if i != 0:
                l, r = i-1, i
                while (l >= 0 and r < len(s) and s[l].lower() == s[r].lower()):
                    l -= 1
                    r += 1
                if (r-l-1 > best):
                    best = r-l-1
                    best_l = l+1
                    best_r = r
        return s[best_l:best_r]
                
            
            
        