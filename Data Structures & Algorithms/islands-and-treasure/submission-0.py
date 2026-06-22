class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        row = len(grid)
        col = len(grid[0])
        inf = 2147483647

        dq = deque([])

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    dq.append((i,j))
                

        while dq:
            r, c = dq.popleft()

            for dr, dc in d:
                nr = dr + r
                nc = dc + c

                if nr < 0 or nr >= row or nc < 0 or nc >= col or grid[nr][nc] == -1:
                    continue

                if grid[nr][nc] == inf:
                    grid[nr][nc] = grid[r][c] + 1
                    dq.append((nr,nc))
