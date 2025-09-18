M = 1000 + 239

sum = 0
a = [False] * M
b = [False] * M
s = [""] * M

T = int(input())
sum = 0

while T > 0:
    T -= 1
    n, m = map(int, input().split())
    sum += n * m
    for i in range(n):
        s[i] = input()

    ch = True
    for i in range(n):
        for j in range(m):
            ch &= (s[i][j] == '0' or s[i][j] == '1')
    assert ch

    for i in range(n):
        a[i] = False
        for j in range(m):
            a[i] |= (s[i][j] == '1')

    for j in range(m):
        b[j] = False
        for i in range(n):
            b[j] |= (s[i][j] == '1')

    ch = False
    for i in range(n):
        ch |= a[i]

    for i in range(n):
        for j in range(m):
            if not ch:
                print(-1, end=' ')
            elif s[i][j] == '1':
                print(0, end=' ')
            elif a[i] or b[j]:
                print(1, end=' ')
            else:
                print(2, end=' ')
        print()

assert sum <= 10**6