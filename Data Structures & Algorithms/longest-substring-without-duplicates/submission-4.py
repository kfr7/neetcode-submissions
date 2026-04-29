class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        longest = 1
        window = set()
        l, r = 0, 0

        while l <= r and l < len(s) and r < len(s):
            print(l, r, window)
            if l != r:
                if s[r] in window:
                    while l < r and s[r] in window:
                        window.remove(s[l])
                        print('moving l right', l, )
                        l += 1
                    # then it will break out and we will now add right into the window again
            window.add(s[r])
            longest = max(longest, len(window))
            r += 1
                
        return longest
                   
            


        