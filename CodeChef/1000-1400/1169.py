# cook your dish here
for t in range(int(input())):
    n,x = map(int,input().split())
    maxi = x
    vals = list(map(int,input().split()))
    for i in vals:
        x += i
        maxi = max(x,maxi)
    print(maxi)