class WordDictionary:

    def __init__(self):
        self.root = dict()
        
    def addWord(self, word: str) -> None:
        curr_level = self.root
        for c in word:
            if c not in curr_level:
                curr_level[c] = dict()
            curr_level = curr_level[c]
        curr_level['end'] = 1
        

    def search(self, word: str) -> bool:
        def helper(curr_level, i): 
            # curr_level we are at
            # i is the index we are searching for in the word
            if i >= len(word):
                if 'end' in curr_level:
                    return True
                return False
            # otherwise we need to see if we are matching and move on if we can
            if word[i] != '.':  # first deal with case where it must match
                if word[i] not in curr_level:
                    return False
                # otherwise move the level up and call the helper again
                return helper(curr_level[word[i]], i+1)
            else:   # loop through all of the keys and call helper on them
                for k in curr_level:
                    if len(k) == 1: # just so we skip the word 'end'
                        if (helper(curr_level[k], i+1)):
                            return True
            return False

        if len(word) == 0:
            return True
        
        return helper(self.root, 0)