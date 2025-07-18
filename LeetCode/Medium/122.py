from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        profit = 0
        while i<len(prices)-1:
            if prices[i+1]>prices[i]:
                profit+= prices[i+1]-prices[i]
            i+=1
        return profit