t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    p=int(input())
    temp=l[p-1]
    l.sort()
    print(l.index(temp)+1)