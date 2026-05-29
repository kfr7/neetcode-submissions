class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(l, r):
            # we are just going to go left and right until we are not equal

            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            
            # when we break out, then the best is:
            return s[l+1:r]
        
        best = ""
        for i in range(len(s)):
            best_response = helper(i, i)
            if i != 0:
                not_centered = helper(i-1, i)
                if len(not_centered) > len(best_response):
                    best_response = not_centered
            if len(best_response) > len(best):
                best = best_response
            
        return best



        # best = ""
        # memo = dict()

        # def dfs(l, r):
        #     if l >= r:
        #         return True # we reached the end of the string
            
        #     if (l, r) in memo:
        #         return memo[(l,r)]
            
        #     if s[l] != s[r]:
        #         memo[(l,r)] = False
        #         return False
            
        #     # otherwise they are equal so it just depends on the rest
        #     memo[(l,r)] = dfs(l+1, r-1)
        #     return memo[(l,r)]
        
        # # now we just need to call it
        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         if dfs(i, j) and j-i+1 > len(best):
        #             best = s[i:j+1]
        
        # return best
        