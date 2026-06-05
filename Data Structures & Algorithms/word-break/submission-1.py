class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # have some sort of recursive helper function
        # that takes in the iteration, when we evenfind a 
        # if we find a word, try to use it and start building a 
        # new word at next index, but also make a call that does not use it
        # and perhaps goes to next index while still building
        # if we are not at a current word, we need to keep expanding
        wordSet = set(wordDict)
        memo = dict()
        # we need l and r so we can construct the word we are at
        def helper(l,r):
            if r == len(s):
                return False    # all dfs will reach the end, valuable is when last char completed some word not if we reached the end
            if (l, r) in memo:
                return memo[(l, r)]
            curr = str(s[l:r+1])
            if curr not in wordSet:   # we have no option but to continue expanding
                memo[(l, r)] = helper(l, r+1)
                return memo[(l, r)]
            else:   # we can either use this word and start over, or continue building
                if r == len(s)-1:
                    memo[(l, r)] = True # since we reached the end and it was a word!
                    return memo[(l, r)]
                else:   # we are not sure yet
                    memo[(l, r)] = helper(r+1, r+1) or helper(l, r+1)
                    return memo[(l, r)]
                
        return helper(0,0)


        
        