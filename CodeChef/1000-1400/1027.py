for _ in range(int(input())):
    n = int(input())
    s = list(input())

    # Swap adjacent pairs
    for i in range(0, n - 1, 2):
        s[i], s[i+1] = s[i+1], s[i]

    # Replace characters
    for i in range(n):
        s[i] = chr(ord('a') + ord('z') - ord(s[i]))

    print("".join(s))