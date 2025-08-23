# cook your dish here
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    r = list(map(int,input().split()))
    a = [l[i]*r[i] for i in range(n)]
    b = [i for i in range(n) if a[i] == max(a)]
    c = [r[i] for i in b]
    print(r.index(max(c))+1)