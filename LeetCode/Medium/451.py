class Solution:
    def frequencySort(self, s: str) -> str:
        frq = Counter(list(s))
        
        sortedChars = sorted(frq.items(),key = lambda x:x[1],reverse = True)

        return "".join([i*j for i,j in sortedChars])