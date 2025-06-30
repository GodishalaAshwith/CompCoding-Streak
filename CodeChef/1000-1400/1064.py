# cook your dish here
for _ in range(int(input())):
    x,y,z = list(map(int,input().split()))
    if x>=y:
        print("PIZZA")
    elif x>=z:
        print("BURGER")
    else:
        print("NOTHING")