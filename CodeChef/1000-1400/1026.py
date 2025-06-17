for _ in range(int(input())):
    n, x = map(int, input().split())
    if x % 2 == 1:
        print("YES")
    else:
        if n % 2 == 0:
            print("YES")
        else:
            print("NO")