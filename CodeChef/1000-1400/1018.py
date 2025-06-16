for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print('Yes' if max(a.count(x) for x in a) <= 2 else 'No')