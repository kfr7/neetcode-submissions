class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        sd, td = dict(), dict()
        for i in range(len(s)):
            if s[i] not in sd:
                sd[s[i]] = 0
            sd[s[i]] += 1
            if t[i] not in td:
                td[t[i]] = 0
            td[t[i]] += 1
        if len(sd) != len(td):
            return False
        for k in sd:
            if k not in td:
                return False
            if sd[k] != td[k]:
                return False
        return True

        
        