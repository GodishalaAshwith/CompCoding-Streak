class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n = len(num)
        good = []
        for i in range(1,n-1):
            if num[i-1]==num[i] and num[i]==num[i+1]:
                good.append(num[i-1:i+2])
        if good:
            return max(good)
        else:
            return ""