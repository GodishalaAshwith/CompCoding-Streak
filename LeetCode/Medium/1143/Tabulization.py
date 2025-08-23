class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n,m = len(text1),len(text2)
        dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0] = 0
        for j in range(m+1):
            dp[0][j] = 0
        
        for i1 in range(1,n+1):
            for i2 in range(1,m+1):
                if text1[i1-1]==text2[i2-1]: dp[i1][i2] = 1 + dp[i1-1][i2-1]
                else: dp[i1][i2] = max(dp[i1-1][i2],dp[i1][i2-1])
        return dp[n][m]