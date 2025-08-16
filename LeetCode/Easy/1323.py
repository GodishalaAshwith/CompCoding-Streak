def firstSix(nstr):
    for i,n in enumerate(nstr):
        if n == "6":
            return i
    return None

class Solution:
    def maximum69Number (self, num: int) -> int:
        nstr = str(num)
        res = list(nstr)
        toChange = firstSix(nstr)
        if toChange is not None:
            res[toChange] = "9"

        return int("".join(res))
