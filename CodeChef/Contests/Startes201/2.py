# cook your dish here
for _ in range(int(input())):
    a,b = map(int,input().split())
    
    quantity = (min(a,b//2))*3
    
    print(quantity)