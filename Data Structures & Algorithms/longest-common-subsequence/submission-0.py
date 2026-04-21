class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]

        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                print(i, j)
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:   # if they don't match then you need the max of leaving character out from one of the texts
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]
                    



        