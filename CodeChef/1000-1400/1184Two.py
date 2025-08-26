# cook your dish here

# Pattern Checking
# 2 => 1, 2
# 3 => 2, 1, 3
# 4 => 2, 3, 1, 4
# 5 => 3, 2, 4, 1, 5
# 6 => 3, 4 ,2, 5, 1, 6
# 7 => 4, 3, 5, 2, 6, 1, 7
# 8 => 4, 5, 3, 6, 2, 7, 1, 8

t = int(input())
for _ in range(t):
    N = int(input())
    Permutation = [(N + 1) // 2]
    i = 1
    while N > 1:
        Permutation.append((-1) ** (N % 2) * i + Permutation[i - 1])
        N -= 1
        i += 1

    Permutation = list(map(str, Permutation))
    print(' '.join(Permutation))