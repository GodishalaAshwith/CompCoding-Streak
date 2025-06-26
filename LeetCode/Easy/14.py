from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = []
        minS = len(min(strs, key=len))

        for i in range(minS):
            current_char = strs[0][i]
            if all(s[i] == current_char for s in strs):
                prefix.append(current_char)
            else:
                break
        return "".join(prefix)