from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        characterCount = defaultdict(int)
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            characterCount[s[i]] += 1
        
        for j in range(len(t)):
            if t[j] not in characterCount:
                return False
            # otherwise subtract it
            characterCount[t[j]] -= 1
            if characterCount[t[j]] == 0:
                del characterCount[t[j]]
        
        return True
        