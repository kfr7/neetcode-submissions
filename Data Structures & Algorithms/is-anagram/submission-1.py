class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        firstCount = dict()
        for ch in s:
            firstCount[ch] = firstCount.get(ch, 0) + 1
        for ch in t:
            if ch in firstCount:
                firstCount[ch] -= 1
                if firstCount[ch] == 0:
                    del firstCount[ch]
            else:
                return False
        return len(firstCount) == 0
        