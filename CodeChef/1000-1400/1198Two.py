# cook your dish here
for _ in range(int(input())):
    n = int(input())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))

    res = 0
    for i in range(n):
        temp = 0
        for j in range(n - i):
            temp += matrix[j + i][j]
        res = max(temp, res)

    for j in range(1, n):
        temp = 0
        for i in range(n - j):
            temp += matrix[i][j + i]
        res = max(res, temp)

    print(res)
