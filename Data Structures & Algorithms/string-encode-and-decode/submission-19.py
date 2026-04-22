class Solution:

    def encode(self, strs: List[str]) -> str:
        all_strs = []
        for string in strs:
            length = len(string)
            all_strs.append(str(length) + '-' + string)
        print(all_strs)
        return ''.join(all_strs)

    def decode(self, s: str) -> List[str]:
        final = []
        reading = False
        build_length = []
        build_word = []
        for ch in s:
            if not reading:
                if ch == '-':
                    build_length = int(''.join(build_length))
                    if build_length == 0:
                        final.append('')
                        build_length = []
                    else:
                        reading = True
                else:
                    build_length.append(ch)
            else: # we are reading in characters
                if build_length == 0:   # short circuit for empty string
                    reading = False
                    final.append('')
                    build_length = []
                    build_word = []
                else:
                    build_word.append(ch)
                    build_length -= 1
                    if build_length == 0:
                        final.append(''.join(build_word))
                        reading = False
                        build_length = []
                        build_word = []
        return final

                

