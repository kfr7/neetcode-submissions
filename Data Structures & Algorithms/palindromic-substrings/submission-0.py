class Solution:
    def countSubstrings(self, s: str) -> int:
        found = 0

        if len(s) == 0:
            return 0

        for i in range(len(s)):
            # first do it with a center
            l, r = i, i
            while (l == r) or (l >= 0 and r < len(s) and s[l].lower() == s[r].lower()):
                found += 1
                l -= 1
                r += 1
            
            # then if it is not the first letter, do it for letters that are adjacent that are the same
            if i != 0:
                l, r = i-1, i
                print(l, r)
                while (l >= 0 and r < len(s) and s[l].lower() == s[r].lower()):
                    found += 1
                    l -= 1
                    r += 1

        return found
        