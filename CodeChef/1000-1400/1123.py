# cook your dish here
t = int(input())
for _ in range(t):
    Length, Parts = map(int, input().split())
    if Length % Parts == 0:
        print(0)
    else:
        print(1)