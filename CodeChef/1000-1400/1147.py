# cook your dish here
for TC in range(int(input())):
    N,K=map(int,input().split())
    d=0
    for j in range(N):
        T,D=map(int,input().split())
        d+=max(T-K,0)*D
        K=max(K-T,0)
    print(d)