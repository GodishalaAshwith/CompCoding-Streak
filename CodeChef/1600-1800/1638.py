def check(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find(n):
    primes = []
    while len(primes) < 2:
        if check(n):
            primes.append(n)
        n += 1
    return primes[0] * primes[1]


t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    if n == 1:
        n += 1
    print(find(n))
