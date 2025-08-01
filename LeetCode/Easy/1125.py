from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            print(res)
            if i == 0:
                pasArr = [1]
            elif i == 1:
                pasArr = [1,1]
            else:
                pasArr = []
                for j in range(i+1):
                    if j == 0:
                        pasArr.append(1)
                    elif j == i:
                        pasArr.append(1)
                    else:
                        pasArr.append(res[i-1][j-1]+res[i-1][j])
            res.append(pasArr)
        return res