class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagRev = {"".join(sorted(string)):[] for string in strs}
        for string in strs:
            anagRev["".join(sorted(string))].append(string)
        res = [v for k,v in anagRev.items()]
        print(res)