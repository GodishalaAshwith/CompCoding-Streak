# cook your dish here
def presolve():
    pass

def solve():
    n = int(input())
    v = list(map(int, input().split()))

    poss = True
    for i in range(1, n):
        if v[i - 1] % v[i] != 0:
            poss = False
            break

    if poss:
        print(' '.join(map(str, v)))
    else:
        print(-1)

T = int(input())
for _ in range(T):
    solve()