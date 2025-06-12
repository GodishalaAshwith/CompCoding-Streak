t = int(input())

while t > 0:
    n = int(input())
    d = list(map(int, input().split()))
    # Your code goes here
    t -= 1
    dS = sorted(d)
    if d == dS:
        print("Yes")
    else:
        print("No")