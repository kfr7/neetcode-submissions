class PrefixTree:

    def __init__(self):
        self.root = dict()

    def insert(self, word: str) -> None:
        curr_level = self.root
        for character in word:
            if character not in curr_level:
                curr_level[character] = dict()
            curr_level = curr_level[character]
        curr_level['end'] = True

    def search(self, word: str) -> bool:
        curr_level = self.root
        for character in word:
            if character not in curr_level:
                return False
            curr_level = curr_level[character]
        if 'end' in curr_level:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        curr_level = self.root
        for character in prefix:
            if character not in curr_level:
                return False
            curr_level = curr_level[character]
        return True
        
        