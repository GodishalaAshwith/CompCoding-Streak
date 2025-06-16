for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    storage = 0
    success = True
    
    for i in range(n):
        storage += a[i]
        if storage < k:
            print("NO", i + 1)
            success = False
            break
        storage -= k
    
    if success:
        print("YES")
