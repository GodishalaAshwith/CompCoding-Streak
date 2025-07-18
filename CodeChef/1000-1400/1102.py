# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    pts = [(i*20) - (j*10) if (i*20) - (j*10) > 0 else 0 for i,j in zip(a,b)]
    print(max(pts))