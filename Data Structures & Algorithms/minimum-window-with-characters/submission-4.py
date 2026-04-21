class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # keep growing it until you satisfy it
        teeFreq = dict()
        for element in t:
            teeFreq[element] = 1 + teeFreq.get(element, 0)
        
        bestLeft = None
        bestRight = None

        esFreq = dict()
        matched = set() # the keys that we correctly have the amounts for

        l, r = 0 , -1

        while r < len(s):
            if len(matched) < len(teeFreq):
                print('if:', ''.join([s[k] for k in range(l, r+1)]), matched)
                # then we need to expand the window
                r += 1
                if r == len(s) or s[r] not in teeFreq:
                    continue
                # otherwise we know we have a valuable character
                esFreq[s[r]] = 1 + esFreq.get(s[r], 0)
                if esFreq[s[r]] == teeFreq[s[r]]:
                    matched.add(s[r])
                # now we may meet the criteria
                if len(matched) == len(teeFreq) and (bestLeft is None or r-l+1 < bestRight-bestLeft+1):
                    bestRight = r
                    bestLeft = l                   
                # else we just continue expanding

            else: # we did meet the criteria so let's try to make it shorter
                print('else:', ''.join([s[k] for k in range(l, r+1)]), matched)
                if s[l] not in teeFreq:
                    l += 1
                    if (bestLeft is None or r-l+1 < bestRight-bestLeft+1):
                        bestRight = r
                        bestLeft = l    
                else:
                    esFreq[s[l]] -= 1
                    if esFreq[s[l]] < teeFreq[s[l]]:
                        matched.remove(s[l])
                        l += 1
                    else:
                        l += 1
                        if (bestLeft is None or r-l+1 < bestRight-bestLeft+1):
                            bestRight = r
                            bestLeft = l

        
        return ''.join([s[k] for k in range(bestLeft, bestRight+1)]) if bestLeft is not None else ""


        