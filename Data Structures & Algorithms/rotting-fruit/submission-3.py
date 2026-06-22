class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # BFS

        di = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        row = len(grid)
        col = len(grid[0])

        fresh = 0
        dq = deque([])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    dq.append((i,j))
        
        if fresh == 0:
            return 0
        count = -1
        
        while dq:
            size = len(dq)
            print(dq)
            for _ in range(size):
                r, c = dq.popleft()
                # visited.add((r, c))
                for dr, dc in di:
                    nr = dr + r
                    nc = dc + c

                    if (nr < 0 or nr >= row or nc < 0 or nc >= col or grid[nr][nc] == 0 or grid[nr][nc] == 2):
                        continue
                    grid[nr][nc] = 2
                    dq.append((nr,nc))
            count += 1
        

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return -1
        return count