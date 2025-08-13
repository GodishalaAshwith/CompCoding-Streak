# cook your dish here
for _ in range(int(input())):
    x1, y1, x2, y2 = map(int,input().split())
    print('NO' if ((x1-x2) + (y1-y2)) %2 else "YES")