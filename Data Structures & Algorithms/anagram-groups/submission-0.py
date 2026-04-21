from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # solution one, sort all of them, N * M log M, but you'd have to map them back so no
        sortedToList = defaultdict(list)
        for element in strs:
            sortedElement = ''.join(sorted(element))
            sortedToList[sortedElement].append(element)
        return sortedToList.values()
        