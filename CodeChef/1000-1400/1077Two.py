def digit_sum(n):
    return sum(int(d) for d in str(n))

def find_next_with_opposite_parity(n):
    original_parity = digit_sum(n) % 2
    x = n + 1
    while digit_sum(x) % 2 == original_parity:
        x += 1
    return x

# Read input
T = int(input())
for _ in range(T):
    N = int(input())
    print(find_next_with_opposite_parity(N))
