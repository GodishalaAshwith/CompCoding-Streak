def solve():
    n = int(input())
    s = input()
    vowels = {'a', 'e', 'i', 'o', 'u'}
    consonant_count = 0
    for char in s:
        if char not in vowels:
            consonant_count += 1
            if consonant_count >= 4:
                print("NO")
                return
        else:
            consonant_count = 0
    print("YES")

t = int(input())
for _ in range(t):
    solve()