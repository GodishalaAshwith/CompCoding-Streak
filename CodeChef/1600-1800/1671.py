MOD = 10 ** 9 + 7


def dfs(adj, visited, src):
    stack = [src]
    cc_total = 0
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            cc_total += 1
            stack.extend(adj[node])
    return cc_total


def solve(n, m, friendships):
    adj = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)

    for x, y in friendships:
        adj[x].append(y)
        adj[y].append(x)  # for undirected graph

    total = 0
    cap = 1

    for j in range(1, n + 1):
        if not visited[j]:
            cc_total = dfs(adj, visited, j)
            total += 1
            cap = (cap * cc_total) % MOD

    print(total, cap)


if __name__ == "__main__":
    import sys

    input = sys.stdin.read
    data = input().splitlines()
    t = int(data[0])
    index = 1
    for _ in range(t):
        n, m = map(int, data[index].split())
        friendships = [tuple(map(int, data[i].split())) for i in range(index + 1, index + 1 + m)]
        solve(n, m, friendships)
        index += 1 + m