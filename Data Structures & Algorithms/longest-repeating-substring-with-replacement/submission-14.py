from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        
        longest = 1
        freq = defaultdict(int) # this is the frequency of the current default dict
        most_freq = 1
        l, r = 0, 0
        while l <= r and r < len(s):
            if l == r:
                freq[s[l]] += 1
                most_freq = max(most_freq, freq[s[l]])
                # base condition will never be longer than longest
                r += 1
            else:   # l != r
                # first always add r to the frequency and then we will check for validitiy
                freq[s[r]] += 1
                most_freq = max(most_freq, freq[s[r]])
                if r-l+1 - most_freq <= k:  # then we have "replacements" to spare
                    longest = max(longest, r-l+1)
                    r += 1
                else:
                    freq[s[r]] -= 1 # just so next loop doesn't increment for no reason
                    freq[s[l]] -= 1
                    l += 1
        return longest

        












        return
        # below is incorrect, what i need is a character frequency map
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        longest = min(k, len(s))
        indexes_replaced = 0    # this will keep track of which ones changed
        l, r = 0, 0
        while l <= r and r < len(s):
            print('longest when entering loop:', longest)
            print(l,r, indexes_replaced)
            # l is always the character i am going to be replacing for
            if l == r:
                print('a')
                indexes_replaced = 0
                longest = max(longest, 1)
                r += 1
                continue
            if indexes_replaced == k:
                if s[r] != s[l]: # stopping condition for the window
                    original_l = s[l]
                    while l < r and original_l == s[l]:
                        print('a1')
                        l += 1
                    # only then do we break out and start the next character we find
                    print('b')
                    indexes_replaced = 0
                elif s[r] == s[l]:
                    print('c')
                    longest = max(longest, r-l+1)
                    r += 1
            elif indexes_replaced < k:
                print('d')
                if s[r] != s[l]:
                    print('d1')
                    indexes_replaced += 1
                longest = max(longest, r-l+1)
                r += 1
        print('longest after existing?', longest)
        return longest                    




        

        