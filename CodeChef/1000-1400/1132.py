for _ in range(int(input())):
    a=list(map(int,input().split()))
    print('YES\n' if a.count(min(a))>=2 else 'NO\n')