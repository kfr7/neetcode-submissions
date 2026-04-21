class Solution:

    def encode(self, strs: List[str]) -> str:
        listOfChars = []
        for element in strs:
            listOfChars.append(str(len(element)))
            listOfChars.append("*")
            listOfChars.append(element)
        return ''.join(listOfChars)

    def decode(self, s: str) -> List[str]:
        print(s)
        originalList = []
        buildNum = []
        buildStr = []
        i = 0
        while i < len(s):
            if s[i] != "*":
                # still figuring out the length of what we need to loop
                buildNum.append(s[i])
                i += 1
            elif s[i] == "*":
                # we hit our delimiter so now loop through
                i += 1            
                # now we can start the iteration
                n = int(''.join(buildNum))
                buildNum = []
                print(s, i, n)
                if n == 0:
                    # don't advance the pointer (starts at next number)
                    originalList.append("")
                else:
                    for _ in range(n):
                        buildStr.append(s[i])
                        i += 1
                    originalList.append(''.join(buildStr))
                    buildStr = []
        return originalList



