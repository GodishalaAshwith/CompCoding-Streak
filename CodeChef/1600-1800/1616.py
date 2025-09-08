# cook your dish here
t = int(input())
for i in range(t):
    n,k,s=map(int,input().split())
    m=s//7
    if k*s>(s-m)*n:
        print("-1")
        continue
    if(k*s)%n==0:
        print((k*s)//n)
    else:
        print((k*s)//n+1)