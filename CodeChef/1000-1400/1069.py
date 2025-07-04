import sys
import math

def simple_sieve(limit):
    prime = [True] * (limit + 1)
    prime[0] = prime[1] = False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if prime[i]:
            for j in range(i*i, limit + 1, i):
                prime[j] = False
    return [i for i, is_prime in enumerate(prime) if is_prime]

def segmented_sieve(m, n, primes):
    size = n - m + 1
    is_prime = [True] * size

    for p in primes:
        start = max(p*p, ((m + p - 1) // p) * p)
        for j in range(start, n + 1, p):
            is_prime[j - m] = False

    result = []
    for i in range(size):
        if is_prime[i] and (m + i) > 1:
            result.append(str(m + i))
    return result

def main():
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    idx = 1
    output = []

    max_limit = 10**5
    primes = simple_sieve(int(math.sqrt(10**9)) + 1)

    for _ in range(t):
        m = int(data[idx])
        n = int(data[idx + 1])
        idx += 2

        segment_primes = segmented_sieve(m, n, primes)
        output.extend(segment_primes)
        output.append('')  # Empty line between test cases

    sys.stdout.write('\n'.join(output).strip() + '\n')

if __name__ == "__main__":
    main()
