# cook your dish here
def solve(N, K, W):
    cnt = 0
    s = 0
    for i in W:
        if i > K:
            return -1
        if s + i <= K:
            s = s + i
        elif s + i > K:
            s = i
            cnt += 1

    return cnt + 1


test = int(input())
while (test > 0):
    N, K = map(int, input().split())
    W = list(map(int, input().split()))
    print(solve(N, K, W))
    test -= 1