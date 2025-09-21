# cook your dish here
for _ in range(int(input())):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [[0] * 3 for _ in range(n)]

    for i in range(n):
        t = 0
        if (a[i] == 1):
            t = 0
        elif (a[i] == 2):
            t = 1
        else:
            t = 2

        if (i == 0):
            dp[i][t] += 1
        else:
            dp[i][0] = dp[i - 1][0]
            dp[i][1] = dp[i - 1][1]
            dp[i][2] = dp[i - 1][2]
            dp[i][t] += 1
            # print(dp)

    for i in range(q):
        l, r = map(int, input().split())
        l = l - 1
        r = r - 1
        if ((r - l + 1) % 2 == 1):
            print("No")
            continue
        if (l >= 1):
            t0 = dp[r][0] - dp[l - 1][0]
            t1 = dp[r][1] - dp[l - 1][1]
            t2 = dp[r][2] - dp[l - 1][2]
        else:
            t0 = dp[r][0]
            t1 = dp[r][1]
            t2 = dp[r][2]
        ls = [t0, t1, t2]
        ls.sort()
        tl = (r - l + 1)
        if (ls[2] == tl // 2):
            print("Yes")
        else:
            print("No")

# [1,2,2,3,3,3,3,3]

