class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dictionary of keys being tuples that demonstrate the chars
        # such as size 26 and value at index represents count for that number
        res = dict()
        for s in strs:
            temp26 = [0] * 26
            for i in range(len(s)):
                temp26[ord(s[i])-97] += 1
            immutable = tuple(temp26)
            if immutable in res:
                res[immutable].append(s)
            else:
                res[immutable] = [s]
        return res.values() 
        