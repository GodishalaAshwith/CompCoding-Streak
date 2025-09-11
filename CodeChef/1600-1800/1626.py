def solve():
    n, k = map(int, input().split())
    s = input()

    last_pos = -1

    def find_farthest(start_color, k):

        curr = 0
        jumps = 0

        for i in range(1, n):
            if s[i] != s[curr]:
                curr = i
                jumps += 1
                if jumps == k:
                    return i + 1
        return -1

    changes = 0
    for i in range(1, n):
        if s[i] != s[i - 1]:
            changes += 1

    if changes < k:
        print(-1)
        return

    last_valid_index = -1
    curr = 0
    jumps = 0

    for i in range(1, n):
        if s[i] != s[curr]:
            curr = i
            jumps += 1
            if jumps == k:
                last_valid_index = i + 1

    target_color_index = 0
    target_jumps = k

    first_color = s[0]

    if k % 2 == 0:
        target_color = first_color
    else:
        target_color = '0' if first_color == '1' else '1'

    ans = -1
    for i in range(n - 1, -1, -1):
        if s[i] == target_color:
            ans = i + 1
            break

    print(ans)


t = int(input())
for _ in range(t):
    solve()