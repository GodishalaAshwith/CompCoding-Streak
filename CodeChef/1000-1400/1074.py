# cook your dish here
for _ in range(int(input())):
    X , Y , Z = list(map(int,input().split()))
    if X == Y + Z or Y == X + Z or Z == X + Y :
        print("yes")
    else:
        print("no")