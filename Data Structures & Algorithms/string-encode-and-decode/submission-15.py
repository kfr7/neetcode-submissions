class Solution:

    def encode(self, strs: List[str]) -> str:
        # count the number of characters in the str and 
        # put a number + the delimiter for when we know when to stop reading the number
        build = []
        for s in strs:
            build.append(str(len(s)))
            build.append(';')
            build.append(s)
        # now concatenate and return it as a string
        print(''.join(build))
        return ''.join(build)

    def decode(self, s: str) -> List[str]:
        result = []
        build_number = []
        curr_i = 0
        while curr_i < len(s):
            if (s[curr_i] != ';'):  # we are still building number
                build_number.append(s[curr_i])
                curr_i += 1
            elif (s[curr_i] == ';'):    # we have reached the end of the delimiter
                curr_i += 1 # skip past the delimiter
                actual_number = int(''.join(build_number))
                build_number = []   # reset the build number for next time
                build_word = []
                print('actual_number and curr_i is at:', actual_number, curr_i)
                for _ in range(actual_number):
                    build_word.append(s[curr_i])
                    curr_i += 1
                # once we build the word
                if len(build_word) == 0:
                    result.append('')
                else:
                    result.append(''.join(build_word))
        return result
                
              

            

