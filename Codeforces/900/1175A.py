def StepsToZero(n, k):
    steps = 0
    while n > 0:
        if k == 1:
            # Can't divide, must subtract 1 every time
            return steps + n
        if n % k == 0:
            n //= k
            steps += 1
        else:
            # Subtract the remainder to reach next divisible point
            remainder = n % k
            n -= remainder
            steps += remainder
    return steps

for _ in range(int(input())):
    n, k = map(int, input().split())
    print(StepsToZero(n, k))
