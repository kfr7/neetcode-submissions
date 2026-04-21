class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            length = len(s)
            strLength = str(length)
            for element in strLength:
                res.append(element)
            res.append(';')

            for element in s:
                res.append(element)
        return ''.join(res)


    def decode(self, s: str) -> List[str]:
        reading = True
        res = []
        strLength = []
        i = 0
        while i < len(s):
            if reading:
                if s[i] != ';':
                    strLength.append(s[i])
                else:
                    actualLength = int(''.join(strLength))
                    reading = False
                    strLength = []
                    if actualLength == 0:
                        res.append('')
                        reading = True
                i += 1
            else:
                res.append(''.join(s[i:i+actualLength]))
                i += actualLength
                reading = True
        return res


            

