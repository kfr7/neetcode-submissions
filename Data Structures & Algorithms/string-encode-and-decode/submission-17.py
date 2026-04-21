class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for word in strs:
            length = str(len(word))
            for element in length:
                res.append(element)
            res.append(';')
            for c in word:
                res.append(c)
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        length = 0
        build_len = []
        i = 0
        res = []
        while i < len(s):
            if s[i] == ';':
                length = int(''.join(build_len))
                build_len = []
                i += 1
                # then here we loop that many times
                build_word = []
                for j in range(length):
                    build_word.append(s[i])
                    i += 1
                res.append(''.join(build_word))
            else:
                build_len.append(s[i])
                i += 1
        return res



