k, r = map(int, input().split())

for n in range(1, 11):
    total = n * k
    if total % 10 == 0 or total % 10 == r:
        print(n)
        break
