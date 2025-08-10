for _ in range(int(input())):
    n = int(input())
    a_arr = list(map(int,input().split()))
    b_arr = list(map(int,input().split()))
    aGreaterThanb = 0
    for i in range(n):
        if a_arr[i]>b_arr[i]:
            aGreaterThanb += a_arr[i] - b_arr[i]
    
    print(aGreaterThanb+1)