class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        characterCount = dict()
        l , r = 0, -1
        longestString = 0
        biggestFrequencyFound = 0
        while r < len(s):
            # len of window - most frequent character
            tempLength = r - l + 1
            # print("longestString", longestString, "biggestFrequencyFound", biggestFrequencyFound, "l", l ,"r", r, "tempLength", tempLength)

            if (tempLength - biggestFrequencyFound) <= k:
                longestString = max(longestString, tempLength)
                r += 1
                # print(s, r)
                if r < len(s):
                    characterCount[s[r]] = 1 + characterCount.get(s[r], 0)
                    biggestFrequencyFound = max(biggestFrequencyFound, characterCount[s[r]])
            else:
                # we exceeded window plus character replacement move left pointer
                characterCount[s[l]] -= 1
                l += 1
        return longestString
