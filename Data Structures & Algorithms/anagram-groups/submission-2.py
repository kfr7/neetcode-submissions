from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we can group them using an array of 26 (index per character)
        # <tuple of 1s and 0s>: [strs that are anagrams]
        ana = dict()
        for s in strs:
            temp = [0 for _ in range(26)]   # [0] * 26 will also work, just can't do it for mutable objects
            # loop through each character and add the needed index
            for el in s:
                temp[ord(el)-97] += 1
            # convert to tuple and add s to that array if it exists 
            val = ana.get(tuple(temp), [])
            val.append(s)
            ana[tuple(temp)] = val
        return ana.values()
            














        # solution one, sort all of them, N * M log M, but you'd have to map them back so no
        sortedToList = defaultdict(list)
        for element in strs:
            sortedElement = ''.join(sorted(element))
            sortedToList[sortedElement].append(element)
        return sortedToList.values()
        