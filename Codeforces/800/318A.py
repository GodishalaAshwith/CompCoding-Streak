n, k = map(int, input().split())

odd_count = (n + 1) // 2  # number of odd numbers

if k <= odd_count:
    print(2 * k - 1)
else:
    print(2 * (k - odd_count))
