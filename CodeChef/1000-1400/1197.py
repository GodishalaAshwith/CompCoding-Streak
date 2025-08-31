# cook your dish here
t = int(input())
for i in range(t):
    n = int(input())
    x = list(map(int, input().split()))
    x.sort()
    c = 0
    for i in range(n):
        if x[i] > i+1:
            print(-1)
            break
        elif x[i] < i+1:
            c += (i+1 - x[i])
    else:
        print(c)