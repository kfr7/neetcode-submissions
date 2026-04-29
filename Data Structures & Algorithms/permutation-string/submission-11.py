from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        letters_needed = set()
        truth = defaultdict(int)
        for element in s1:
            letters_needed.add(element)
            truth[element] += 1
        copy = letters_needed.copy()
        l, r = 0, 0
        window = defaultdict(int)
        while l <= r and r < len(s2):
            if s2[r] not in truth:
                l += 1
                r += 1
                window = defaultdict(int) # reset
                letters_needed = copy.copy()
            else:   # otherwise we have a chance this will work
                window[s2[r]] += 1
                print(window)
                if window[s2[r]] < truth[s2[r]]:
                    print('a')
                    r += 1
                elif window[s2[r]] == truth[s2[r]]:
                    print('b')
                    letters_needed.remove(s2[r])
                    print(len(letters_needed))
                    if len(letters_needed) == 0:
                        return True
                    r += 1
                elif window[s2[r]] > truth[s2[r]]:    #invalid
                    print('c')
                    window[s2[l]] -= 1
                    window[s2[r]] -= 1
                    if window[s2[l]] < truth[s2[l]]:
                        letters_needed.add(s2[l])
                    l += 1
        return False

                

               



                
                    