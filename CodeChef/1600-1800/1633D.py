t = int(input())
while (t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    s = 0
    add = True
    for i in a:
        if i == 1 or s <= 1 or add:
            s += i
            add = False
        else:
            s *= i

        s = s % 1000000007

    print(s)

    t -= 1