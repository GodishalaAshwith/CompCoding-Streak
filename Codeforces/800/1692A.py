t = int(input())
for _ in range(t):
    a, b, c, d = map(int, input().split())
    count = 0
    for x in [b, c, d]:
        if x > a:
            count += 1
    print(count)
