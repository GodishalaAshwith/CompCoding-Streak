n, t = map(int, input().split())
q = list(input())

for _ in range(t):
    i = 1
    while i < n:
        if q[i-1] == 'B' and q[i] == 'G':
            q[i-1], q[i] = q[i], q[i-1]
            i += 2  # Skip the next position to avoid double-swap
        else:
            i += 1

print("".join(q))
