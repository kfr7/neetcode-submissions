class Solution:
    def longestPalindrome(self, s: str) -> str:
        best = ""
        memo = dict()

        def dfs(l, r):
            if l >= r:
                return True # we reached the end of the string
            
            if (l, r) in memo:
                return memo[(l,r)]
            
            if s[l] != s[r]:
                memo[(l,r)] = False
                return False
            
            # otherwise they are equal so it just depends on the rest
            memo[(l,r)] = dfs(l+1, r-1)
            return memo[(l,r)]
        
        # now we just need to call it
        for i in range(len(s)):
            for j in range(i, len(s)):
                if dfs(i, j) and j-i+1 > len(best):
                    best = s[i:j+1]
        
        return best
        