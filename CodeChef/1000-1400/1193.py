# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    s=sum(a)//(n+1)
    b=[]
    for x in a:
        b.append(x-s)
    print(*b)