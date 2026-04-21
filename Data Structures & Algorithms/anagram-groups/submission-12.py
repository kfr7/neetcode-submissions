from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we only care about the frequency,
        # we know it is only 26 characters, so let's use the indexes
        # as a hash map and use that to use as keys and the value will be arrays of strings with this mapping
        d = defaultdict(list)
        for el in strs:
            temp = [0] * 26
            for letter in el:
                # print(letter, ord(letter))
                temp[ord(letter)-97] += 1
                print('temp after:', temp)
            # now we have something like [3, 0, 2, 1, 0, 0, ...]
            print('-'.join(str(n) for n in temp))
            d['-'.join(str(n) for n in temp)].append(el)
        
        print(d)
        return d.values()



        