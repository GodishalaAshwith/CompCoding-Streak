class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        n = len(s)
        res = [s[i:i+k] for i in range(0,n,k) ]
        if len(res[-1])!=k:
            filling = k - len(res[-1]) 
            res[-1] = res[-1]+fill*filling
        return res      