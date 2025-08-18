import math
for _ in range(int(input())):
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    s,m=0,0
    for i in range(n):
        s += math.ceil(a[i]/x)
    m = max(a)    
    print(min(s,m))