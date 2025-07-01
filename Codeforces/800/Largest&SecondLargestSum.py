t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    t -= 1
    # Your code goes here
    a1 = max(a)
    a = [i for i in a if i!=a1]
    a2 = max(a)
    print(a1+a2)