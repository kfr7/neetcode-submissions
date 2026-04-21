from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = defaultdict(int)
        for element in s:
            first[element] += 1
        
        print(first)
        # now go through the second word and subtract
        for element in t:
            if element not in first:
                return False
            first[element] -= 1
            if first[element] == 0:
                del first[element]

        if len(first) != 0:
            return False
        return True

        