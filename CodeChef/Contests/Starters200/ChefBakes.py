# cook your dish here
def solve(n,x,y):
    res = (n+(y//x)-1)//(y//x)
    print(res)

n,x,y = map(int,input().split())
solve(n,x,y)