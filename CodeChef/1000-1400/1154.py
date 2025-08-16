def minxor(a,b):
    xor=0
    for i in range(a):
        xor=xor^b[i]
    ans=xor
    for i in range(a):
        ans=min(ans,xor^b[i])
    return ans

if __name__=="__main__":
    for _ in range(int(input())):
        a=int(input())
        b=list(map(int,input().split()))
        print(minxor(a,b))