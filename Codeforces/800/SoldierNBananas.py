k,n,w = list(map(int,input().split()))
costs = sum([i*k for i in range(1,w+1)])
print(costs-n) if costs-n > 0 else print(0)