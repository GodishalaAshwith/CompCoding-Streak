# cook your dish here
for T in range(int(input())):
    x, y, n, r = map(int,input().split())
    ans = [0,0]
    if r < x * n:
        print(-1)
        next
    elif r >= y * n:
        print(0, n)
        next
    else:
        ans[1] = min(n,(r-x*n)//(y-x))
        ans[0] = n - ans[1]
        print(*ans)