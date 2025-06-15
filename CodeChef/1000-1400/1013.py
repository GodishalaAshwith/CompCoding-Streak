# cook your dish here
t = int(input())

while t > 0:
    t-=1
    #cook here
    n = int(input())
    b = list(map(int,input().split()))
    if b.count(1) % 2==0:
        print("YES")
    else:
        print("NO")