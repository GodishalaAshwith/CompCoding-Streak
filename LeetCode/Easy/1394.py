from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        frq = Counter(arr)
        luckyList = [i for i,j in frq.items() if i==j]
        if luckyList:
            return max(luckyList)
        else:
            return -1