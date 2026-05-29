class Solution:
    def countSubstrings(self, s: str) -> int:
        memo = dict()
        def dfs(l, r):
            if l > r:
                return True # because if it got here everything was equal
            
            if (l, r) in memo:
                return memo[(l,r)]
            
            if s[l] != s[r]:
                memo[(l, r)] = False
                return memo[(l, r)]
            
            # otherwise they are equal so this is good but depends on inner
            memo[(l, r)] = dfs(l+1, r-1)
            return memo[(l,r)]

        
        for i in range(len(s)):
            for j in range(i, len(s)):
                dfs(i, j)
        
        # then we will just loop through the memo at the end
        count = 0
        for _, v in memo.items():
            if v:
                count +=1

        return count

        