class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        vP = {'[':']', '(':')', '{':'}'}
        
        for i in s:
            if i in vP:
                stk.append(i)
            elif stk and vP[stk[-1]] == i:
                stk.pop()
            else:
                return False 
                
        return not stk 