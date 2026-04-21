class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Freq = dict()
        for element in s1:
            s1Freq[element] = 1 + s1Freq.get(element, 0)
        
        # now sliding window for s2 and keep track of s2Freq and when we add or 
        # remove a character, we need to check if we met the criteria of s1
        # we can just have a set of the keys that we HAVE matched so that we can check the length of it against s1Freq

        l, r = 0, -1
        s2Freq = dict()
        matchingKeys = set()

        while r < len(s2):
            print(s2Freq, (r - l + 1), len(s1), matchingKeys) 
            if (r - l + 1) < len(s1):
                r += 1
                if r < len(s2):
                    s2Freq[s2[r]] = 1 + s2Freq.get(s2[r], 0)
                    if s2[r] in s1Freq and s2Freq[s2[r]] == s1Freq[s2[r]]:
                        matchingKeys.add(s2[r])
                        if len(matchingKeys) == len(s1Freq):
                            return True
                    elif s2[r] in matchingKeys: # it may have been equal before so try to remove it
                            matchingKeys.remove(s2[r])
            else:
                # we are at the length and we know we don't match so move left to the right
                s2Freq[s2[l]] -= 1
                # this may have caused us to lose our match
                if s2[l] in matchingKeys:
                    matchingKeys.remove(s2[l])
                #  (or gain it back)
                elif s2[l] in s1Freq and s2Freq[s2[l]] == s1Freq[s2[l]]:
                    matchingKeys.add(s2[l])
                l += 1
        return False

        