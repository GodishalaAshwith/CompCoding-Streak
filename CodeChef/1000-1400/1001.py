T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    result = ''
    for amount in A:
        if K >= amount:
            K -= amount
            result += '1'
        else:
            result += '0'
    print(result)
