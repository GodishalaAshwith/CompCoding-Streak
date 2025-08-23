def f(s1,s2,i1,i2,dp):
    if i1<0 or i2<0: return 0

    if dp[i1][i2] !=-1: return dp[i1][i2]

    if s1[i1]==s2[i2]: dp[i1][i2] = 1 + f(s1,s2,i1-1,i2-1,dp)
    else: dp[i1][i2] = max(f(s1,s2,i1-1,i2,dp),f(s1,s2,i1,i2-1,dp))

    return dp[i1][i2]

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]
        return f(text1,text2,len(text1)-1,len(text2)-1,dp)