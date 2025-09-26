# cook your dish here
for _ in range(int(input())):
    x, y = map(int, input().split())
    if y >= x-1: ans = 1
    elif 2*y >= x-1: ans = 2
    else: ans = x-2*y
    print(ans)