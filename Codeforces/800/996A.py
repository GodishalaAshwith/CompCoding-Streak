n = int(input())
count = 0
for d in [100, 20, 10, 5, 1]:
    count += n // d
    n %= d
print(count)
