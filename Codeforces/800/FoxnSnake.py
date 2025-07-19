n,m = map(int,input().split())

res = [['.' for _ in range(m)] for _ in range(n)]

for i in range(0,n,2):
    res[i][:] = ["#"]*m

for i in range(1,n,4):
    res[i][m-1]="#"

if n>3:
    for i in range(3,n,4):
        res[i][0]="#"

for i in res:
    print(*i)