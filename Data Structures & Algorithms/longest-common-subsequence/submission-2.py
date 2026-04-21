class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {} # will store i, j keys
        def dfs(i, j):
            if i >= len(text1) or j >= len(text2):
                # nothing in common so return 0
                dp[(i, j)] = 0
            else:   # they are both in range so see if they match here
                if ((i, j) not in dp):
                    if text1[i] == text2[j]:
                        if ((i+1, j+1) in dp):
                            dp[(i, j)] = 1 + dp[(i+1, j+1)]
                        else:   # then we need to compute it
                            dp[(i, j)] = 1 + dfs(i+1, j+1)
                    else:   # if they are not equal then we need to see which route is better
                        skipText1 = float('-inf')
                        if ((i+1, j) in dp):
                            skipText1 = dp[(i+1, j)]
                        else:
                            skipText1 = dfs(i+1, j)
                        skipText2 = float('-inf')
                        if ((i, j+1) in dp):
                            skipText2 = dp[(i, j+1)]
                        else:
                            skipText2 = dfs(i, j+1)
                        dp[(i, j)] = max(skipText1, skipText2)
            return dp[(i, j)]

        dfs(0, 0)
        return dp[(0, 0)]
                    

                        




        # if we were to use dfs though it would be the above
        # dp = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]

        # for i in range(len(text1)-1, -1, -1):
        #     for j in range(len(text2)-1, -1, -1):
        #         print(i, j)
        #         if text1[i] == text2[j]:
        #             dp[i][j] = 1 + dp[i+1][j+1]
        #         else:   # if they don't match then you need the max of leaving character out from one of the texts
        #             dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        # return dp[0][0]
                    



        