import math

t = int(input())
for _ in range(t):
    a, b, c, d = list(map(int, input().split()))
    lcm = math.lcm(b, d)
    gcd = math.gcd(b, d)
    ans = lcm
    rem = a % b
    if (b - rem - 1) >= 1 and (d - rem - 1) >= 1:
        print(1)
    else:
        print(ans - rem)
