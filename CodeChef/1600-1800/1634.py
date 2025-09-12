def binexp(a, b, CC):
    res = 1
    while b:
        if b & 1:
            res = (res * a) % CC
        a = (a * a) % CC
        b >>= 1
    return res

def problem():
    CC = 10**9 + 7  # Modulus value
    n, m = map(int, input().split())
    ans = binexp(2, n, CC) - 1
    ans = binexp(ans, m, CC)
    print(ans)

t = int(input())
for _ in range(t):
    problem()