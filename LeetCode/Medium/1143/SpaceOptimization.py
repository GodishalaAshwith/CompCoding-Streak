class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n,m = len(text1),len(text2)
        prev = [0]*(m+1)
        cur = [0]*(m+1)

        
        for i1 in range(1,n+1):
            for i2 in range(1,m+1):
                if text1[i1-1]==text2[i2-1]: cur[i2] = 1 + prev[i2-1]
                else: cur[i2] = max(prev[i2],cur[i2-1])
            prev = cur[:]
        return prev[m]