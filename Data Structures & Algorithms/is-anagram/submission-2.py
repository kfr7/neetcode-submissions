class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charCount = dict()
        for character in s:
            charCount[character] = 1 + charCount.get(character, 0)
        
        # now go through t and make sure to subtract charCount
        for character in t:
            if character not in charCount:
                return False
            # otherwise continue subtracting
            charCount[character] -= 1
            if charCount[character] == 0:
                del charCount[character]
        return len(charCount) == 0
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
        