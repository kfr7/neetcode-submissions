class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        for string in strs:
            result = [0] * 26
            for s in string:
                result[ord(s)-97] += 1
            result = [str(x) for x in result]
            stringResult = "-".join(result)
            if stringResult not in d:
                d[stringResult] = [string]
            else:
                d[stringResult].append(string)
        return list(d.values())
        