def equalize(a, b, x):
    if (a - b) % (2 * x) == 0:
        return "YES"
    else:
        return "NO"

for _ in range(int(input())):
    a, b, x = map(int, input().split())
    print(equalize(a, b, x))