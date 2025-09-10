# cook your dish here
for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    if n == 1:
        print(0)
    else:
        fm = l[-1]
        sm = 0
        for i in range(n - 1, -1, -1):
            if l[i] < fm:
                sm = l[i]

                break
        print(sm)

