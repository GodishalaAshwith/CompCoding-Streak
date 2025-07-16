t=int(input())
for i in range(t):
    N=int(input())
    l=list(map(int,input().split()))
    d={}
    for k in l:
        if k in d:
            d[k]+=1
        else:
            d[k]=1
    m=max(d.values())
    print(N-m)
        