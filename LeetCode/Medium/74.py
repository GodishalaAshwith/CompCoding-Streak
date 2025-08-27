class Solution(object):
    def searchMatrix(self, matrix, target):
        r=len(matrix)
        c=len(matrix[0])
        a=0
        b=(r*c)-1
        while a<=b:
            m=(a+b)//2
            x=m//c
            y=m%c
            if matrix[x][y]==target:
                return True
            elif matrix[x][y]<target:
                a=m+1
            else:
                b=m-1
        return False