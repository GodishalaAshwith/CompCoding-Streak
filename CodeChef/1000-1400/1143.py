t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    s = input()
    if s[0]=='0':
        s = '1'+s[1:]
        s+='0'*(k-1)
    else:
        s+='0'*k
    print(s)