def lessgo():
    n, m, k = map(int, input().split())

    v = {}
    for _ in range(k):
        r, c = map(int, input().split())
        r -= 1
        c -= 1
        v[(r, c)] = 1

    ans = 0
    for (i, j) in v.keys():
        ok1 = False
        ok2 = False

        if i > 0 and v.get((i - 1, j), 0) == 1:
            ok1 = True
        if j > 0 and v.get((i, j - 1), 0) == 1:
            ok2 = True

        if ok1 and ok2:
            continue
        elif ok1 or ok2:
            ans += 2
        else:
            ans += 4

    print(ans)


test = int(input())
for _ in range(test):
    lessgo()
    print()