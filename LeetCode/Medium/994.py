class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        num_fresh = 0
        q = collections.deque()
        for i in range(n):
            for j in range(m):
                num_fresh += (grid[i][j] == 1)
                if grid[i][j] == 2:
                    q.append((i, j))

        ans = 0
        while q and num_fresh > 0:
            ans += 1
            to_add = []
            while q:
                i, j = q.popleft()
                for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if i + x >= 0 and i + x < n and j + y >= 0 and j + y < m and grid[i + x][j + y] == 1:
                        grid[i + x][j + y] = 2
                        num_fresh -= 1
                        to_add.append((i + x, j + y))
            q.extend(to_add)

        return -1 if num_fresh > 0 else ans





