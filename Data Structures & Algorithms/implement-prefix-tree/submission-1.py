class PrefixTree:

    def __init__(self):
        self.t = dict()
        

    def insert(self, word: str) -> None:
        current_level = self.t
        for i in range(len(word)):
            letter = word[i]
            if letter not in current_level:
                current_level[letter] = dict()
            if i == len(word) - 1:
                current_level[letter]["end"] = True
            current_level = current_level[letter]

    def search(self, word: str) -> bool:
        current_level = self.t
        for i in range(len(word)):
            letter = word[i]
            if letter not in current_level:
                return False
            else:   # it is in the current_level
                # if it is the last letter, check if end is there
                if i == len(word) - 1:
                    if "end" in current_level[letter]:
                        return True
                    else:
                        return False
                else:   # simply in the middle of building the word still
                    current_level = current_level[letter]
        return False # should not hit

    def startsWith(self, prefix: str) -> bool:
        # similar to search but can stop early
        current_level = self.t
        for i in range(len(prefix)):
            letter = prefix[i]
            if letter not in current_level:
                return False
            else:
                current_level = current_level[letter]
        return True
        
        